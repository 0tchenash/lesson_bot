from db.utils_db import WeekdayDAO
from services.week_service import WeekService
from db.setup_db import session

week_dao = WeekdayDAO(session=session)
week_services = WeekService(dao=week_dao)