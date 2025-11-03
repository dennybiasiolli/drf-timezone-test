# check console width for this query

echo "Check console width for this query, if it wraps, try increasing console width"
read -p "Press [Enter] key to continue..."

# get the script path
script_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

psql drf_timezone_test -f "$script_path/01-create-sql-table.sql"
psql drf_timezone_test -f "$script_path/03-insert-db-values.sql"

psql drf_timezone_test -c "select to_char(value_dt, 'YYYY-"Q"Q') as quarter, * from test_timezone order by value_dt;"

# wait for user input
read -p "Has the output wrapped? [y/N]: " wrap_answer
if [[ "$wrap_answer" == "y" || "$wrap_answer" == "Y" ]]; then
    echo "Please increase your console width and re-run the script."
    exit 1
elif [[ "$wrap_answer" == "" || "$wrap_answer" == "n" || "$wrap_answer" == "N" ]]; then
    echo "Great! Proceeding..."
else
    echo "Invalid input. Please enter 'y' or 'n'."
    exit 1
fi

read -p "Do you want to reset the database and re-apply migrations? [y/N]: " reset_answer
if [[ "$reset_answer" == "y" || "$reset_answer" == "Y" ]]; then
    echo "Resetting database..."
    dropdb drf_timezone_test && \
        createdb -U denny -T template0 drf_timezone_test
    uv sync --all-groups
    uv run python manage.py migrate
    uv run python manage.py createsuperuser
    echo "Database reset and migrations applied."
elif [[ "$reset_answer" == "" || "$reset_answer" == "n" || "$reset_answer" == "N" ]]; then
    echo "Skipping database reset."
else
    echo "Invalid input. Please enter 'y' or 'n'."
    exit 1
fi
