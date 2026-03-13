from config import FORCE_SUB, BUTTONS_PER_ROW, BUTTONS_JOIN_TEXT
from pyrogram.types import InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

async def start_button(client):
    if not FORCE_SUB:
        return [
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")]
        ]

    dynamic_buttons = []
    current_row = []

    for key in FORCE_SUB.keys():
        current_row.append(
            InlineKeyboardButton(
                text=f"{BUTTONS_JOIN_TEXT} {key}",
                url=getattr(client, f"invitelink{key}")
            )
        )
        if len(current_row) == BUTTONS_PER_ROW:
            dynamic_buttons.append(current_row)
            current_row = []

    if current_row:
        dynamic_buttons.append(current_row)

    dynamic_buttons.append(
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")]
    )

    return dynamic_buttons


async def fsub_button(client, message):
    if FORCE_SUB:
        user_id = message.from_user.id
        dynamic_buttons = []
        current_row = []

        for key, channel_id in FORCE_SUB.items():
            try:
                # Cek status member secara real-time
                await client.get_chat_member(channel_id, user_id)
                # Jika sudah join, lewati tombol ini
                continue
            except UserNotParticipant:
                # Jika belum join, tambahkan ke baris tombol
                current_row.append(
                    InlineKeyboardButton(
                        text=f"{BUTTONS_JOIN_TEXT} {key}",
                        url=getattr(client, f"invitelink{key}")
                    )
                )
            except Exception:
                # Jika error lain, tetap tampilkan tombol agar aman
                current_row.append(
                    InlineKeyboardButton(
                        text=f"{BUTTONS_JOIN_TEXT} {key}",
                        url=getattr(client, f"invitelink{key}")
                    )
                )

            if len(current_row) == BUTTONS_PER_ROW:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)

        # Tambahkan tombol Coba Lagi jika masih ada channel yang perlu di-join
        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ])
        except (IndexError, AttributeError):
            pass

        return dynamic_buttons
async def fsub_button(client, message):
    if FORCE_SUB:
        user_id = message.from_user.id
        dynamic_buttons = []
        current_row = []

        for key, channel_id in FORCE_SUB.items():
            # Cek apakah user sudah join
            try:
                await client.get_chat_member(channel_id, user_id)
                # Jika berhasil/tidak error, berarti sudah join.
                # Kita 'continue' agar tombol ini tidak dimasukkan ke daftar.
                continue
            except UserNotParticipant:
                # Jika error ini muncul, berarti BELUM join.
                # Masukkan ke baris tombol.
                current_row.append(
                    InlineKeyboardButton(
                        text=f"{BUTTONS_JOIN_TEXT} {key}",
                        url=getattr(client, f"invitelink{key}")
                    )
                )
            except Exception:
                # Jika ada error lain (misal bot bukan admin), tetap tampilkan agar aman.
                current_row.append(
                    InlineKeyboardButton(
                        text=f"{BUTTONS_JOIN_TEXT} {key}",
                        url=getattr(client, f"invitelink{key}")
                    )
                )

            if len(current_row) == BUTTONS_PER_ROW:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)

        # Tambahkan tombol Coba Lagi jika masih ada channel yang belum di-join
        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ])
        except IndexError:
            pass

        return dynamic_buttons    return dynamic_buttons


def fsub_button(client, message):
    if FORCE_SUB:
        dynamic_buttons = []
        current_row = []

        for key in FORCE_SUB.keys():
            current_row.append(
                InlineKeyboardButton(
                    text=f"{BUTTONS_JOIN_TEXT} {key}",
                    url=getattr(client, f"invitelink{key}")
                )
            )
            if len(current_row) == BUTTONS_PER_ROW:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)

        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ])
        except IndexError:
            pass

        return dynamic_buttons
