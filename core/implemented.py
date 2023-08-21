from db.utils_db import WeekdayDAO
from services.week_service import WeekService
from db.models import DaysSchema
from db.setup_db import session

week_dao = WeekdayDAO(session=session)
week_services = WeekService(dao=week_dao)
week_schemas = DaysSchema(many=True)