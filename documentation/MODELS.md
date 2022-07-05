# HolbertonBnB - Models Class System :cl:

HolbertonBnB supports the following classes:

* [BaseModel](../models/base_model.py)
* [User](../models/user.py)
* [State](../models/state.py)
* [City](../models/city.py)
* [Amenity](../models/amenity.py)
* [Place](../models/place.py)
* [Review](../models/review.py)

<p align="center">
  <img src="https://github.com/bdbaraban/HolbertonBnB/blob/master/assets/hbnb-models.png"
       alt="HolbertonBnB logo"
       width="750"
  >
</p>

[Source code.](../models)

## Storage :baggage_claim:

The above classes are handled by one of either two abstracted storage engines,
depending on the call - [FileStorage](../models/engine/file_storage.py) or
[DBStorage](../models/engine/db_storage.py).

### FileStorage


