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

import boto3
import hashlib
from django.conf import settings
from ndingest.settings.settings import Settings
ndingest_settings = Settings.load()

def generateS3Key(project_name, channel_name, resolution, morton_index, time_index=0):
  """Generate the key for the supercube"""

  hashm = hashlib.md5()
  hashm.update('{}&{}&{}&{}&{}'.format(project_name, channel_name, resolution, morton_index, time_index))
  return '{}&{}&{}&{}&{}&{}'.format(hashm.hexdigest(), project_name, channel_name, resolution, morton_index, time_index)

def generateS3BucketName():
  """Return the S3 Bucket Name for the project"""

  # return '{}'.format(settings.S3_CUBOID_BUCKET)
  return '{}'.format(ndingest_settings.S3_CUBOID_BUCKET)

# def getSuperCubes(ch, proj, listofidxs, resolution):
  # """Get the SuperCube from the backend"""

  # for zidx in listofidxs:
    # super_listofidxs.add(generateSuperZindex(zidx, resolution))
  
  # for super_zidx in super_listofidxs:
    # self.client.get_object(Bucket=generateS3BucketName(proj.getProjectName, ch.getChannelName()), Key=self.generateS3Key(zidx,resolution)).get('Body').read()
    # return breakCubes
