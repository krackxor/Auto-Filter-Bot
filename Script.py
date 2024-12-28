import os
class script(object):

    START_TXT = """<b><i>ʜʏ {} {},

ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇ ᴇᴀʀɴ ꜰᴇᴀᴛᴜʀᴇ.
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴀɴʏ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ ᴏʀ ᴀɴɪᴍᴇ ɪɴ ɢʀᴏᴜᴘ ʙʏ ʏᴏᴜʀ ᴄᴏɴ�[...]

ʏᴏᴜʀ ɪᴅ -<code> {}</code></i></b>"""

    HELP_TXT = """<b><i>Klik pada tombol di bawah untuk mendapatkan dokumentasi tentang modul spesifik..[...]"""

    CODEXBOTS = """<b><i>/upload - kirim saya gambar atau video di bawah (5MB)

Catatan - Perintah ini hanya bekerja di PM</i></b>"""

    STATUS_TXT = """<b><u>🗃 Basis Data 1 🗃</u>

» Total pengguna - <code>{}</code>
» Total grup - <code>{}</code>
» Penyimpanan yang digunakan - <code>{} / {}</code>

<u>🗳 Basis Data 2 🗳</u></b>

» Total file - <code>{}</code>
» Penyimpanan yang digunakan - <code>{} / {}</code>

<u>🤖 Detail Bot 🤖</u>

» Waktu aktif - <code>{}</code>
» RAM - <code>{}%</code>
» CPU - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#Pengguna_Baru

≈ ID:- <code>{}</code>
≈ Nama:- {}</b>"""

    NEW_GROUP_TXT = """#Grup_Baru

Nama grup - {}
Id - <code>{}</code>
Username grup - @{}
Link grup - {}
Total anggota - <code>{}</code>
Pengguna - {}"""

    IMDB_TEMPLATE_TXT = """<b>📻 Judul - <a href={url}>{title}</a>
🎭 Genre - {genres}
🎖 Peringkat - <a href={url}/ratings>{rating}</a> / 10 (berdasarkan {votes} peringkat pengguna.)
📆 Tahun - {release_date}
❗️ Bahasa - {languages}</b>
"""

    FILE_CAPTION = """<b><a href=https://telegram.me/TechifyBots>{file_name} </a></b>

<i>Silakan teruskan file ini ke pesan yang disimpan dan tutup pesan ini</i>"""

    RESTART_TXT = """<b>
📅 Tanggal : <code>{}</code>
⏰ Waktu : <code>{}</code>
🌐 Zona Waktu : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """❌ Itu bukan untuk Anda sir ⛔️"""

    OLD_ALRT_TXT = """Anda menggunakan salah satu pesan lama saya, silakan kirim t[...]"""

    NO_RESULT_TXT = """🗳 Film ini belum dirilis atau ditambahkan ke datab[...]"""

    I_CUDNT = """🤧 Halo {}

Saya tidak dapat menemukan film atau seri apa pun dengan nama itu.. 😐"""

    I_CUD_NT = """😑 Halo {}

Saya tidak dapat menemukan apa pun yang terkait dengan itu 😞... periksa ejaan Anda[...]"""

    CUDNT_FND = """🤧 Halo {}

Saya tidak dapat menemukan apa pun yang terkait dengan itu apakah Anda maksudkan apapun[...]"""

    FONT_TXT= """<b><i>Anda dapat menggunakan mode ini untuk mengubah gaya font Anda.</i></b>

<code>/font hi how are you</code>"""

    PREMIUM_TEXT = """<b><i><blockquote>Rencana yang tersedia ♻️</blockquote>

• 1 minggu - Rp 5.000
• 1 bulan - Rp 20.000
• 3 bulan - Rp 50.000
• 6 bulan - Rp 75.000

•─────•─────────•─────•
<blockquote>Fitur premium 🎁</blockquote>

○ Tidak perlu verifikasi
○ File langsung
○ Pengalaman bebas iklan
○ Tautan unduhan berkecepatan tinggi
○ Tautan streaming multi-pemain
○ Film, seri & anime tidak terbatas
○ Dukungan admin penuh
○ Permintaan akan selesai dalam 1 jam
•─────•─────────•─────•

✨ ID UPI - <code>TechifyBots@UPI</code>

Periksa rencana aktif Anda /myplan

💢 Harus mengirim tangkapan layar setelah pembayaran

‼️ Setelah mengirim tangkapan layar, beri saya waktu untuk menambahkan Anda ke versi premium[...]"""

    EARN_TEXT = """<b><i><blockquote>Cara menghasilkan uang dengan bot ini 🤑</blockquote>

›› Langkah 1 : Anda harus memiliki setidaknya satu grup dengan minimal 300 anggota.

›› Langkah 2 : Jadikan <a href=https://telegram.me/{}</a> admin di grup Anda.

›› Langkah 3 : Buat akun di <a href='https://tnshort.net/ref/devilofficial'>tnlink</a> atau <a href='https://onepagelink.in/ref/Nobita'>onepage[...]"""

    VERIFICATION_TEXT = """<b>Hai {} {},

Anda belum diverifikasi hari ini 😐
Klik pada verifikasi dan dapatkan akses tak terbatas hingga verifikasi berikutnya

#verifikasi:- 1/3

<blockquote>Jika Anda ingin file langsung maka Anda dapat mengambil layanan premium. (tidak perlu verifikasi)</blo[...]"""

    VERIFY_COMPLETE_TEXT = """<b>Hai {},

Anda telah menyelesaikan verifikasi pertama...

Sekarang Anda memiliki akses tak terbatas hingga verifikasi berikutnya ❤️‍🔥

Jika Anda ingin file langsung tanpa verifikasi, beli langganan kami 😁

💶 Periksa /rencana untuk membeli langganan</b>"""

    SECOND_VERIFICATION_TEXT = """<b>Hai {} {},

Anda belum diverifikasi hari ini 😐
Klik pada verifikasi dan dapatkan akses tak terbatas hingga verifikasi berikutnya

#verifikasi:- 2/3

<blockquote>Jika Anda ingin file langsung maka Anda dapat mengambil layanan premium. (tidak perlu verifikasi)</blo[...]"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>Hai {},

Anda telah menyelesaikan verifikasi kedua...

Sekarang Anda memiliki akses tak terbatas hingga verifikasi berikutnya ❤️‍🔥

Jika Anda ingin file langsung tanpa verifikasi, beli langganan kami 😁

💶 Periksa /rencana untuk membeli langganan</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>Hai {} {},

Anda belum diverifikasi ‼️
Tap pada tautan verifikasi dan dapatkan akses tak terbatas untuk hari ini 😇

#verifikasi:- 3/3

<blockquote>Jika Anda ingin file langsung maka Anda dapat mengambil layanan premium. (tidak perlu verifikasi)</blo[...]"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>Hai {},

Anda sekarang diverifikasi untuk hari ini ☺️

Nikmati film, seri, atau anime tanpa batas 💥

Jika Anda ingin file langsung tanpa verifikasi, beli langganan kami 😁

💶 Periksa /rencana untuk membeli langganan</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ Pengguna diverifikasi berhasil ☄</u>

⚡️ Nama:- {} [ <code>{}</code> ]
📆 Tanggal:- <code>{} </code></b>

#verifikasi_{}_selesai"""

    CUSTOM_TEXT = """<b><i>😊 <u>Semua perintah grup Anda</u> 😊

/shortlink - untuk mengatur pemendek
/shortlink2 - untuk mengatur pemendek untuk verifikasi 2
/shortlink3 - untuk mengatur pemendek untuk verifikasi 3
/time2 - untuk mengatur waktu verifikasi pemendek kedua
/time3 - untuk mengatur waktu verifikasi pemendek ketiga
/log - untuk mengatur saluran log untuk data pengguna
/tutorial - untuk mengatur tautan video tutorial pertama
/tutorial2 - untuk mengatur tautan video tutorial kedua
/tutorial3 - untuk mengatur tautan video tutorial ketiga
/caption - untuk mengatur keterangan file khusus
/template - untuk mengatur template IMDb khusus
/fsub - untuk mengatur saluran langganan paksa Anda
/nofsub - untuk menghapus saluran langganan paksa
/ginfo - untuk memeriksa detail grup Anda</i></b>

😘 Jika Anda melakukan semua ini maka grup Anda akan sangat keren..."""

    FSUB_TXT = """{},

<i><b>🙁 Pertama bergabunglah dengan saluran kami kemudian Anda akan mendapatkan film, jika tidak Anda tidak akan mendapatkannya.

Klik tombol Gabung sekarang 👇</b></i>"""

    DONATE_TXT = """<blockquote>❤️‍🔥 Terima kasih telah menunjukkan minat dalam Donasi</blockq[...]

<b><i>💞 Jika Anda menyukai bot kami, jangan ragu untuk menyumbang dalam jumlah berapa pun.</i[...]

❣️ Donasi sangat dihargai itu membantu dalam pengembangan bot[...]

💖 ID UPI : <code>TechifyBots@UPI</code>
"""
