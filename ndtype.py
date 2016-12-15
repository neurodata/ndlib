# Copyright 2014 NeuroData (http://neurodata.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

# SuperCube Size Multiples
SUPERCUBESIZE = [4,4,4]

# ND Servers
LOCALHOST = 'localhost'
ND_servermap = {'localhost':'localhost'}

# ND_Channel Types, Mapping, Groups
IMAGE = 'image'
ANNOTATION = 'annotation'
TIMESERIES = 'timeseries'
OLDCHANNEL = 'oldchannel'

ND_channeltypes = {0:IMAGE,1:ANNOTATION,2:TIMESERIES,3:OLDCHANNEL}

IMAGE_CHANNELS = [ IMAGE, OLDCHANNEL ]
TIMESERIES_CHANNELS = [ TIMESERIES ]
ANNOTATION_CHANNELS = [ ANNOTATION ]

# ND Data Types, Mapping, Groups
UINT8 = 'uint8'
UINT16 = 'uint16'
UINT32 = 'uint32'
UINT64 = 'uint64'
FLOAT32 = 'float32'
INT8 = 'int8'
INT16 = 'int16'
INT32 = 'int32'

DTYPE_uint8 = [ UINT8 ]
DTYPE_uint16 = [ UINT16 ]
DTYPE_uint32 = [ UINT32 ]
DTYPE_uint64 = [ UINT64 ]
DTYPE_float32 = [ FLOAT32 ]

ND_dtypetonp = {UINT8:np.uint8, UINT16:np.uint16, UINT32:np.uint32, UINT64:np.uint64, FLOAT32:np.float32, INT8:np.uint8, INT16:np.uint16, INT32:np.uint32}

# ND KeyValue,MetaData Engines
MYSQL = 'MySQL'
CASSANDRA = 'Cassandra'
RIAK = 'Riak'
DYNAMODB = 'DynamoDB'
REDIS = 'Redis'

# ND Version
ND_VERSION = '1.0'
SCHEMA_VERSION = '0.7'

# Propagated Values
PROPAGATED = 2
UNDER_PROPAGATION = 1
NOT_PROPAGATED = 0

# ReadOnly Values
READONLY_TRUE = 1
READONLY_FALSE = 0

# SCALING OPTIONS
ZSLICES = 0
ISOTROPIC = 1
ND_scalingtoint = {'zslices':ZSLICES, 'xyz':ISOTROPIC}

# Exception Values
EXCEPTION_TRUE = 1
EXCEPTION_FALSE = 0

# Public Values
PUBLIC_TRUE = 1
PUBLIC_FALSE = 0

# S3 Backend Values
S3_TRUE = 1
S3_FALSE = 0

# Backup Values
FILE_SYSTEM = 'local'
AMAZON_S3 = 's3'

# Ingest Status Values
INGEST_STATUS_PREPARING = 0
INGEST_STATUS_UPLOADING = 1
INGEST_STATUS_COMPLETE = 2
INGEST_STATUS_DELETED = 3
