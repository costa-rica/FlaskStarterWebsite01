# Flask Starter Website 01

![Flask and DashAndData Logo](https://venturer.dashanddata.com/get_aux_file_from_dir/images/dd_and_flask.png)

## Description
This is the framework for the typical website I use.


## Documentation
This uses MySQL and in order to create the tables you must do it from a terminal:
```
from sqlalchemy import create_engine
from fsw_models import Base,engine
from fsw_config import ConfigWorkstation
config = ConfigWorkstation()
new_engine_str = f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_SERVER}/{config.MYSQL_DATABASE_NAME}"
new_engine = create_engine(new_engine_str)
Base.metadata.create_all(new_engine)
```
