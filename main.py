import os
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated
import zoneinfo

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Query, Request
from sqlmodel import (
    Column,
    TIMESTAMP,
    Field,
    Session,
    SQLModel,
    create_engine,
    func,
    select,
    asc,
)

# Load environment variables from .env
load_dotenv()


class TimezoneTestBase(SQLModel):
    value_str: str = Field(max_length=50)
    value_dt: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False)
    )
    comment: str = Field(max_length=100)


class TimezoneTest(TimezoneTestBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class TimezoneTestPublic(TimezoneTestBase):
    id: int


class TimezoneTestCreate(TimezoneTestBase):
    pass


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

engine = create_engine(os.getenv("DATABASE_URL", ""))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code can go here
    create_db_and_tables()
    yield
    # cleanup code can go here


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def check_timezone_header_or_cookie(request: Request, call_next):
    tz_header = request.headers.get("X-Timezone")
    tz_cookie = request.cookies.get("fastapi_timezone")

    tz = "UTC"  # default timezone
    if tz_header:
        tz = tz_header
    elif tz_cookie:
        tz = tz_cookie

    # check timezone validity
    try:
        zoneinfo.ZoneInfo(tz)
    except zoneinfo.ZoneInfoNotFoundError:
        tz = "UTC"

    request.state.tz = tz

    response = await call_next(request)
    return response


@app.post("/api/timezone-tests/", response_model=TimezoneTestPublic)
def create_timezone(timezone: TimezoneTestCreate, session: SessionDep):
    db_timezone = TimezoneTest.model_validate(timezone)
    session.add(db_timezone)
    session.commit()
    session.refresh(db_timezone)
    return db_timezone


@app.get("/api/timezone-tests/")
async def read_timezones(
    request: Request,
    session: SessionDep,
    value_dt__gte: Annotated[datetime | None, Query(example="2025-01-01")] = None,
    value_dt__lt: Annotated[datetime | None, Query(example="2025-04-01")] = None,
):
    tz = zoneinfo.ZoneInfo(request.state.tz)

    results = session.exec(
        select(TimezoneTest)
        .where(
            (
                (
                    func.timezone(request.state.tz, TimezoneTest.value_dt)
                    >= value_dt__gte
                )
                if value_dt__gte
                else True
            ),
            (
                (func.timezone(request.state.tz, TimezoneTest.value_dt) < value_dt__lt)
                if value_dt__lt
                else True
            ),
        )
        .order_by(asc(TimezoneTest.value_dt))
    ).all()

    # Convert value_dt to the requested timezone
    for result in results:
        result.value_dt = result.value_dt.astimezone(tz)
    return results
