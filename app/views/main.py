#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
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
#


from flet_core import Text, Container, alignment, Column, Row, Image
from flet_manager.utils import get_svg

from app.controls import View
from app.utils import Fonts


class MainView(View):
    route = '/'

    async def build(self):
        self.bgcolor = '#121212'
        self.controls = [
            Column(
                controls=[
                    Container(
                        content=Text(
                            value='Flet Manager',
                            font_family=Fonts.SEMIBOLD,
                            color='#ffffff',
                            size=32,
                        ),
                        expand=True,
                        alignment=alignment.center,
                    ),
                    Container(
                        content=Row(
                            controls=[
                                Container(
                                    content=Image(
                                        src=get_svg('assets/icons/github.svg'),
                                        width=48,
                                        height=48,
                                        tooltip='GitHub',
                                    ),
                                    url='https://github.com/yegoryakubovich/flet_manager',
                                ),
                                Container(
                                    content=Image(
                                        src=get_svg('assets/icons/pypi.svg'),
                                        width=48,
                                        height=48,
                                        tooltip='PyPI',
                                    ),
                                    url='https://pypi.org/project/flet-manager',
                                ),
                            ],
                            tight=True,
                            spacing=16,
                        ),
                        alignment=alignment.center,
                    ),
                ],
                expand=True,
            ),
        ]
