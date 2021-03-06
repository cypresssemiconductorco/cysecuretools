"""
Copyright (c) 2019 Cypress Semiconductor Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from abc import ABC, abstractmethod


class PolicyParserBase(ABC):
    """
    Base class for the classes that implement policy parser.
    Each device-specific policy parser must implement its methods.
    """
    @abstractmethod
    def get_keys(self, out=None, image_type=None, key_type=None):
        pass

    @abstractmethod
    def get_image_data(self, image_type, image_id):
        pass

    @abstractmethod
    def get_slot(self, slot_id):
        pass

    @abstractmethod
    def get_cybootloader_mode(self):
        pass

    @abstractmethod
    def get_provisioning_packet_dir(self):
        pass
