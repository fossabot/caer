# Copyright 2020 The Caer Authors. All Rights Reserved.
#
# Licensed under the MIT License (see LICENSE);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at <https://opensource.org/licenses/MIT>
#
# ==============================================================================

#pylint:disable=undefined-all-variable

from ._meta import version as v
from ._meta import author as __author__
from ._meta import release as r
from ._meta import contributors as c
__version__ = v
__contributors__ = c
__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2020 Jason Dsouza'
version = v
release = r
contributors = c

from .preprocess import * 
from .utilities import * 
from .opencv import * 
from .visualizations import * 
# from .time import * 
from .images import * 
from .configs import * 

from .data import *
from .preprocessing import *
from .utils import *
from .video import *



# # __all__ configs
# from .configs import __all__ as __all_configs__
# from .images import __all__ as __all_images__
# from .opencv import __all__ as __all_opencv__
# from .preprocess import __all__ as __all_preprocess__
# from .time import __all__ as __all_time__
# from .utilities import __all__ as __all_utilities__
# from .visualizations import __all__ as __all_visualizations__

# # from .io import __all__ as __all_io__
# from .video import __all__ as __all_video__
# from .preprocessing import __all__ as __all_preprocessing__
# from .data import __all__ as __all_data__
# from .utils import __all__ as __all_utils__
# from .path import __all__ as __all_path__


# __all__ = __all_configs__ + __all_images__ + __all_opencv__ + __all_preprocess__ + __all_time__ + __all_utilities__ + __all_visualizations__

# __all__ += __all_preprocessing__ 
# __all__ += __all_video__ 
# __all__ += __all_data__ 
# __all__ += __all_utils__ 
# __all__ += __all_path__