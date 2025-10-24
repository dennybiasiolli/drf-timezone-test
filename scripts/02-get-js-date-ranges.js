// import { DateTime } from "luxon";
const { DateTime } = require("luxon");

/**
 * Get the start and end date of a quarter in a specific timezone.
 * @param {number} year - The year of the quarter.
 * @param {number} quarter - The quarter number (1-4).
 * @param {string} timezone - The timezone to use.
 * @returns {[string, string]} - An array containing the start and end date of the quarter in ISO format.
 */
function quarterRangeInTimezone(year, quarter, timezone) {
  const startOfQuarter = DateTime.fromObject(
    { year: year, month: (quarter - 1) * 3 + 1, day: 1 },
    { zone: timezone },
  );
  const endOfQuarter = startOfQuarter.endOf("quarter");
  return [startOfQuarter.toISO(), endOfQuarter.toISO()];
}

quarterRangeInTimezone(2025, 1, "America/New_York");
// [ "2025-01-01T00:00:00.000-05:00", "2025-03-31T23:59:59.999-04:00" ]
quarterRangeInTimezone(2025, 1, "Europe/Rome");
// [ "2025-01-01T00:00:00.000+01:00", "2025-03-31T23:59:59.999+02:00" ]
quarterRangeInTimezone(2025, 1, "Asia/Calcutta"); // India Standard Time (IST)
// [ "2025-01-01T00:00:00.000+05:30", "2025-03-31T23:59:59.999+05:30" ]
quarterRangeInTimezone(2025, 1, "Asia/Tokyo");
// [ "2025-01-01T00:00:00.000+09:00", "2025-03-31T23:59:59.999+09:00" ]
