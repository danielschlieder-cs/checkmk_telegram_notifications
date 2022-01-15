#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2021 Stefan Gehn <stefan+cmk@srcbox.net>
#
# SPDX-License-Identifier: GPL-2.0-only

from cmk.gui.valuespec import Dictionary, TextAscii
from cmk.gui.plugins.wato import notification_parameter_registry, NotificationParameter


@notification_parameter_registry.register
class NotificationParameterTelegram(NotificationParameter):
    @property
    def ident(self):
        return "telegram"

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            required_keys=["bot_token", "chat_id"],
            elements=[
                (
                    "bot_token",
                    TextAscii(
                        title=_("Bot Token"),
                        help=_("Telegram Bot Token for sending notifications"),
                        size=46,
                        allow_empty=False,
                    ),
                ),
                (
                    "chat_id",
                    TextAscii(
                        title=_("Chat ID"),
                        help=_("Telegram Chat ID to send notifications to"),
                        size=24,
                        allow_empty=False,
                    ),
                ),
            ],
        )
