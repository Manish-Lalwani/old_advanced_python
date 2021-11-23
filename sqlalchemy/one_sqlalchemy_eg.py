from sqlalchemy import create_engine
from typing import Dict,List,TypeVar,Callable,Optional

SqlalchemyEngine = TypeVar('sqlalchemy.engine.base.Engine')

class SqlalchemyEngineInitializer:
    def __init__(self):
        self._engine_param:Dict[str:Optional[str]] = {
                                                        'user': None,
                                                        'password': None,
                                                        'database': None,
                                                        'hostname': None    }
        self._engine_pool: Dict[str:Callable] = {
                                                "sqlite": self._sqlite_engine_init,
                                                "postgres": self._postgres_engine_init,
                                                "mysql": self._mysql_engine_init,
                                                "oracle": self._oracle_engine_init  }

    def _set_engine_params(self,params:Dict[str, Optional[str]]):
        """SETS CLASS ENGINE PARAMETERS"""
        self._engine_param['user'] = params['user']
        self._engine_param['password'] = params['password']
        self._engine_param['database'] = params['database']
        self._engine_param['database'] = params['database']

    def _postgres_engine_init(self) -> SqlalchemyEngine:
        """RETURNS POSTGRES SQLALCHEMY ENGINE OBJECT"""
        return create_engine(f"postgresql+psycopg2://{self._engine_param['user']}:{self._engine_param['password']}@{self._engine_param['hostname']}/{self._engine_param['database']}")

    def _sqlite_engine_init(self) -> SqlalchemyEngine:
        """RETURNS SQLITE SQLALCHEMY ENGINE OBJECT """
        return create_engine(f"sqlite://{self._engine_param['user']}:{self._engine_param['password']}@{self._engine_param['hostname']}/{self._engine_param['database']}")

    def _mysql_engine_init(self) -> SqlalchemyEngine:
        """RETURNS MYSQL SQLALCHEMY ENGINE OBJECT """
        return create_engine(f"mysql://{self._engine_param['user']}:{self._engine_param['password']}@{self._engine_param['hostname']}/{self._engine_param['database']}")
    def _oracle_engine_init(self) -> SqlalchemyEngine:
        """RETURNS POSTGRES SQLALCHEMY ENGINE OBJECT """
        return create_engine(f"oracle://{self._engine_param['user']}:{self._engine_param['password']}@{self._engine_param['hostname']}/{self._engine_param['database']}")

    def initialize_engine(self,vendor:str,user:str,password:str,database:str,hostname:str='localhost'):
        """Initializes the engine as per given vendor Factory Pattern"""
        self._set_engine_params(params={'user':user,'password':password,'database':database,'hostname':hostname})
        return self._engine_pool.get(vendor)





if __name__ == "__main__":
    obj1 = SqlalchemyEngineInitializer()
    engine = obj1.initialize_engine(user='postgres',password='griffyn',vendor="postgres",database='dpa1')
    print(engine)