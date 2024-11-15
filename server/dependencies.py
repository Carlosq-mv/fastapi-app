from fastapi import Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from actions.dal.userDAO import UserDAO 
from actions.services.userServices import UserServices


def get_db():
    """ Creates and yields a new database session for each request.
    
        This function uses FastAPI's dependency injection system to provide
        a database session to route handlers. The session is automatically
        closed once the request is finished.
        
        The `SessionLocal()` object represents a session factory bound to
        the database, and `yield` is used to return the session to the route
        while ensuring it gets closed after the request is completed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
def get_user_services(db: Session = Depends(get_db)) -> UserServices:
    """ Provides an instance of UserServices for handling user-related operations.
    
        This function is used by FastAPI's dependency injection system to inject
        an instance of the `UserServices` class into the route handlers that
        require it. The `UserDAO` (data access object) is created with the provided
        database session (`db`), and `UserServices` is initialized with `UserDAO`.

    Args:
        db (Session, optional): The database session injected by FastAPI's Depends. 
                                Defaults to Depends(get_db).

    Returns:
        UserServices: An instance of the UserServices class, which handles
        user-related logic, such as user registration, login, and logout.
    """
    dao = UserDAO(db)
    return UserServices(dao)