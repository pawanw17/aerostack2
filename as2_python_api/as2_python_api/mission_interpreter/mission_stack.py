"""
mission_stack.py
"""

# Copyright 2022 Universidad Politécnica de Madrid
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


__authors__ = "Pedro Arias Pérez"
__copyright__ = "Copyright (c) 2022 Universidad Politécnica de Madrid"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"

from collections import deque
from typing import Deque, Tuple

# TODO: improve mission_stack
# Class MissionStack:
#       attributtes: current, done_deque, todo_deque
#       methods: append, insert, repeat_last


class MissionStack:
    """Mission stack"""

    def __init__(self, mission_stack: list = None) -> None:
        mission_stack = [] if mission_stack is None else mission_stack

        # TODO, think if use Deque[MissionItem]
        # Tuples represent MissionItem (behavior, args)
        self.__pending: Deque[Tuple[str, str]] = deque(mission_stack)  # FIFO
        self.__done: Deque[Tuple[str, str]] = deque()  # LIFO
        self.__current: Tuple[str, str] = None

    def next(self):
        if self.__current is not None:
            self.__done.append(self.__current)

        if len(self.pending) > 0:
            self.__current = self.__pending.popleft()
        else:
            self.__current = None
        return self.__current

    def previous(self):
        raise NotImplementedError

    def add(self, item):
        self.__pending.append(item)

    @property
    def last_done(self):
        return self.__done[0]

    @property
    def pending(self) -> list:
        return list(self.__pending)

    @property
    def done(self) -> list:
        return list(self.__done)

    @property
    def current(self):
        # TEMP: use MissionItem instead Tuple
        if self.__current is None:
            return None
        return self.__current[0]
