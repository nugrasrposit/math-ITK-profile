import streamlit as st

# Navigasi antara halaman
with st.sidebar:
    st.image("mathitk.png", width=250)
st.sidebar.title("PROTOTYPE MATEMATIKA ITK")
pages = ["Pengantar Matematika", "Halaman Utama"]
page = st.sidebar.radio("Pilih Halaman", pages)
st.sidebar.title("Kanal Resmi Matematika ITK")
st.sidebar.markdown("[YouTube](https://youtube.com/@mathematicsitkofficial1821)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/mathitk_official/)")
st.sidebar.markdown("[Website](https://math.itk.ac.id)")
st.sidebar.title("Others")
st.sidebar.markdown("[Geogebra](https://geogebra.org)")
st.sidebar.markdown("[MatLab](https://matlab.mathworks.com/?elqsid=qpx0y0s77v104yvkuv2w)")

if page == "Halaman Utama":
    def hitung_skor(ketertarikan_coding, ketertarikan_teonan, ketertarikan_statko, ketertarikan_uang, option, lomba):
        skor = 0
        
        # Menghitung skor berdasarkan ketertarikan (slider 0-100)
        ketertarikan_total = ketertarikan_coding + ketertarikan_teonan + ketertarikan_statko + ketertarikan_uang
        skor += ketertarikan_total / 4 * 0.5   # 50% dari ketertarikan
        
        # Menambahkan skor jika pernah mengikuti lomba
        if lomba == "Yes":
            skor += 20  # 20 poin jika pernah mengikuti lomba
        
        if option == "Ya":
            skor += 30
        elif option == "Terjawab 2 Soal":
            skor += 20
        elif option == "Terjawab 1 Soal":
            skor += 10
        else:
            skor += 0  

        # Skala akhir (0 - 100), bisa dikalibrasi lebih lanjut
        return skor

    def halaman_utama():   
        # Header aplikasi
        st.title("Apakah Anda punya minat terpendam di Matematika?")

        st.subheader("Halaman ini akan membantu kamu untuk mengukur daya tertarik Anda dengan Matematika.")
        st.subheader("Sebelumnya, mari kita tes kecil-kecilan terlebih dahulu.")

        st.write("""1. Seorang petani harus menyeberangi sungai dengan serigala, kambing, dan kubis. Dia memiliki perahu
        yang hanya bisa membawa dirinya sendiri dan salah satu barangnya dalam satu waktu. Jika dibiarkan bersama,
        serigala akan memakan kambing, dan kambing akan memakan kubis. Bagaimana cara petani menyeberangi ketiga sungai
        dengan aman?""")

        st.write("""2. Dua mobil saling mendekat dari arah berlawanan, yang satu bergerak dengan kelajuan 20 m/s dan yang lainnya 
        dengan kelajuan 25 m/s, sepanjang jalan lintasan tunggal yang lurus. Jaraknya 100 m ketika pengemudi saling melihat dan menginjak
        rem. Misalkan setiap mobil mampu melambat sebesar 5 m/s^2 (dan jalan mempunyai tembok tinggi di kedua sisinya), tentukan apakah
        tabrakan tidak dapat dihindari.""")

        st.write("""3. Sebuah pelampung plastik dijatuhkan ke dalam saluran air limbah dan diketahui menempuh jarak 10 kaki dalam waktu 5 detik.
        Saluran ini panjang 4 kaki dan kedalaman alirannya 2 kaki. Hitung laju aliran air limbah ini dalam kaki kubik per detik.""")

        option = st.selectbox("Terjawab Semuanya?", ["Ya", "Terjawab 2 Soal", "Terjawab 1 Soal", "Tidak"])
        
        # Input bagian 1: Ketertarikan terhadap ilmu-ilmu terapan matematika
        st.subheader("Pusing? Bersantai sebentar yuk. Anda sudah pernah mendengar ilmu-ilmu di bawah ini? Setelah dijelaskan, seberapa tertarik Anda dengan ilmu-ilmu tersebut?:")

        st.write(""" **1. Pemrograman** """)
        col1, col2 = st.columns(2)
        with col1:
            st.image("image.png", caption="Honkai: Star Rail", use_container_width=True)
        with col2:
            st.image("ml.jpg", caption="Mobile Legends: Bang Bang", use_container_width=True)  
        
        col3, col4 = st.columns(2)
        with col3:
            st.image("tlok.png", caption="Traveloka", use_container_width=True)
        with col4:
            st.image("chatgpt.png", caption="ChatGPT", use_container_width=True)
        
        st.write("""
                 Zaman sekarang, semua hal serba menggunakan aplikasi. Coba kalian liat aplikasi atau game berikut. Kalian pasti ngga asing dengan game-game, aplikasi, dan AI tersebut kan? Aplikasi ini tidak
                 semerta-merta dibuat langsung jadi begitu saja. Ada proses coding atau pemrograman di dalamnya.
                 Pemrograman itu sendiri dasarnya adalah logika matematika. Web yang kalian lihat ini aja dibuat menggunakan
                 pemrograman. Bahkan, ada beberapa game atau aplikasi yang sudah menggunakan AI di dalamnya.

                 Pemrograman sendiri dasarnya seperti orang tua Anda memerintahkan Kamu untuk melakukan sesuatu hal, misalkan untuk beli bahan-bahan. Banyak sekali
                 hal yang bisa orang tua atau bahkan Kamu lakukan, seperti membuat aplikasi itu sendiri, makan, dll. Pemrograman pun punya prinsip yang sama. Walaupun
                 terlihat rumut, pemrograman ini sebenarnya punya 1 dasar utama, yakni terkait dengan logika. Penjelasan simpelnya jika A, maka B

                 Tadi disinggung terkait dengan AI, apa itu AI kak? Singkatnya, AI atau kecerdasan buatan ini adalah teknologi yang membuat mesin atau komputer bisa berpikir dan belajar seperti manusia.
                 Taukah kamu? AI atau **Artificial Intelligence** ini di dalam pengembangannya, banyak banget menggunakan ilmu-ilmu Matematika sebagai fondasi utamanya.
                 Statistika, Aljabar Linier, Kalkulus, Optimasi menjadi ilmu-ilmu yang banyak digunakan dalam membuat AI. Lalu, cara kerja AI ini bagaimana? Cara kerjanya
                 seperti kita atau manusia belajar dan berpikir. Pasti ada momen yang di mana manusia ini mengumpulkan data
                 untuk misalkan belajar dari kesalahan masa lalu kan? AI bekerja dengan cara yang serupa.
                 Contoh yang paling dekat aja, TikTok. Bagaimana bisa aplikasi tau apa yang kita suka di TikTok itu? Padahal kita ngga ada bilang ke appnya, bahwa kita suka ke konten
                 ini misalkan. Asalnya dari mana? Ya dari si AI ini. 
                 """)
    
        ketertarikan_coding = st.slider("Bagaimana? Setelah dijelaskan, seberapa minat kamu dengan ilmu Pemrograman ini?", 0, 100, 50)  # Slider dari 0 hingga 100

        st.write("""  **2. Teori Permainan** """)
        st.image("catur.jpg", caption="Permainan Catur", use_container_width=True)
        st.write("""
                 Taukah kamu? Main game seperti catur, atau bahkan game yang ada di atas itu juga ada strateginya. Contoh aja, kalau kalian main catur seperti gambar
                 di atas. Jika kamu melakukan pergerakan terhadap bidakmu, maka pasti akan berpengaruh terhadap lawanmu, kira-kira
                 harus membuat pergerakan seperti apa. Inilah yang dimaksud dengan teori permainan.
                 
                 Teori permainan itu sendiri adalah cara untuk mempelajari dan membuat keputusan terhadap apa yang terjadi saat itu.
                 Tujuan adanya teori permainan ini adalah untuk mencari strategi yang tepat untuk hasil terbaik. Biasanya ini juga
                 digunakan di dunia industri. Contoh lain, perang harga dari 2 atau lebih toko dengan menjual barang yang sama. Jika dua
                 toko tersebut sama-sama menurunkan harga, maka mereka akan mendapat sedikit keuntungan, tapi jika hanya satu yang
                 menurunkan harga, dia akan mendapat lebih banyak pelanggan. 
                 
                 Teori permainan ini dasarnya memerlukan logika dan reasoning untuk menganalisis dan menghitung semua kemungkinan yang terjadi.
                 Bahasa lainnya, agar bisa 1 langkah di depan lawan kita. Teori permainan ini juga dapat membantu dalam pengambilan keputusan
                 yang harus diambil. Jadi, udah siap untuk memenangkan permainan lebih banyak dengan teori permainan ini?
                 """)

        ketertarikan_teonan = st.slider("Bagaimana? Apakah berkesan? Seberapa berkesan kamu dengan ilmu ini?", 0, 100, 50)  # Slider dari 0 hingga 100
        st.write("""  **3. Peramalan dan Pemodelan** """)

        col5, col6 = st.columns(2)
        with col5:
            st.image("ramal.png", caption="Ilustrasi Perkiraan Cuaca", use_container_width=True)
        with col6:
            st.image("covid.png", caption="Peramalan COVID-19", use_container_width=True)

        st.write("""
                 Apa? Meramal? Bisa jadi dukun gitu kita? Ngga jadi dukun juga sih sebenarnya. Sebelum ke penjelasan, 
                 apakah pernah terlintas di pikiran, bagaimana badan-badan seperti BMKG dapat memprediksi cuaca
                 secara akurat? Atau bisa juga berkaca dari COVID-19 kemarin, bagaimana ramalan-ramalan ini tercipta?

                 Iyap, ini merupakan contoh dari metode peramalan, salah satu skill khusus yang biasanya dipunyai mahasiswa Matematika.
                 Yang namanya meramal, pasti tujuannya untuk memprediksi apa yang terjadi di masa depan. Tidak hanya peramalan cuaca,
                 peramalan terkait dengan penyebaran virus seperti COVID-19 juga dapat menggunakan metode ini. Dalam proses melakukan peramalan ini, kita melihat data dari masa lalu dan saat ini, dengan tujuan untuk
                 mengetahui pola di balik data-data tersebut, sehingga peramalan tersebut dapat dibuat menjadi sebuah pemodelan.

                 Sesuai dengan namanya, pemodelan ini adalah gambaran atau representasi dari suatu hal yang ada di sekitar. 
                 Pemodelan ini menghubungkan dua variabel atau lebih untuk dapat menentukan kira-kira setelahnya apa
                 yang terjadi ke depannya. Misalkan lagi, kamu ingin tahu kapan tiket konser akan habis terjual. Jika
                 kamu tahu setiap tahun tiketnya terjual 500 lembar per hari setelah diumumkan, kamu bisa meramalkan berapa lama
                 waktu yang dibutuhkan untuk sold out berdasarkan data tersebut. """)

        ketertarikan_ramal = st.slider("Masih berkesan? Seberapa? Bisa jadi 'dukun' loh ", 0, 100, 50) # Slider dari 0 hingga 100
        
        st.write("""**4. Keuangan**""")
        st.image("cicilan1.jpg", width=700, caption="Harga Handphone (2020)")
        st.write("""
                 Hayoo, siapa di sini yang beli hpnya nyicil??? Masa HP aja dicicil sih?? Coba kita lihat ilustrasi ini yaa:
                 Coba kita bandingkan harga HP aslinya, misalkan OPPO A1k 2/32 ini dengan masing-masing berapa kali cicilannya.
                  Asumsikan DP+Admin ini dimasukkan ke dalam uang untuk membayar cicilan ini, maka total harga yang harus dibayarkan
                 adalah Rp2.032.000 untuk 6 bulan dan Rp. 2.338.000 untuk 9 bulan. Kok bisa jauh dengan harga aslinya? Ini yang
                 dinamakan sebagai Suku Bunga.
                 
                 Suku Bunga tidak hanya ada di pembelian HP saja, tetapi juga yang paling kentara terdapat di bank. 
                 Jika anak SMA itu menabung uang di bank atau memiliki pinjaman (misalnya untuk membeli barang atau
                 biaya pendidikan), mereka akan berurusan dengan yang namanya bunga. Ini adalah contoh matematika yang
                 sering digunakan dalam keuangan. Misalnya, jika mereka menabung uang di bank dengan bunga 5% per tahun,
                 itu artinya mereka akan mendapatkan tambahan uang setiap tahun berdasarkan jumlah uang yang mereka simpan.
                 
                 Taukah kamu? Kalau mau masuk ke dunia perbankan, salah satu tes yang akan diujikan adalah berkaitan dengan matematika,
                 terutama terkait dengan logika dan problem solving. Bayangkan aja bagaimana kalian bekerja di Bank seperti apa.
                 Sebenarnya, logika ini termasuk hal yang paling dasar dan mudah untuk terbentuknya ilmu-ilmu yang ada saat ini.
                 Di Matematika ITK, mahasiswanya terbiasa untuk melukan pemecahan masalah.
                 """)
        ketertarikan_uang = st.slider("Mindblowing ngga? Seberapa mindblowing penjelasan tadi?", 0, 100, 50) # Slider dari 0 hingga 100
        st.write("""
                 Ilmu-ilmu tersebut juga dipelajari di program studi Matematika ITK. Sebenarnya, masih banyak
                 ilmu-ilmu dari Matematika ini yang menjadi fondasi ilmu pengetahuan saat ini, dijelaskan di Matematika ITK. Kriptografi, Statistika, bahkan Bilangan itu sendiri dipelajari di sini.
                 Jadi, Matematika tidak hanya tentang kalkulus, pembuktian, 
                 dan logika saja.
                 
                 Secara prospek kerja pun, Matematika ini mempunyai prospek yang bagus dan bisa masuk di mana aja, apalagi dengan zaman yang semua
                 serba menggunakan AI. Bisa di BMKG, jadi data scientist, AI Engineer, dll.""")
        # Input bagian 2: Apakah pernah mengikuti lomba
        st.subheader("2. Apakah Anda pernah mengikuti lomba-lomba terkait matematika? atau ilmu-ilmu tersebut?")
        lomba = st.selectbox("Pilih Jawaban", ["Yes", "No"])

        # Tombol untuk menghitung dan menampilkan hasil
        if st.button("Hitung Skor Ketertarikan"):
            skor = hitung_skor(ketertarikan_coding, ketertarikan_teonan, ketertarikan_ramal, ketertarikan_uang, option, lomba)
            
            # Menampilkan hasil
            st.subheader("Hasil Skor Ketertarikan Anda:")
            st.write(f"Skor Ketertarikan Anda: {skor:.2f} / 100")
            
            if skor >= 70:
                st.write("Anda memiliki ketertarikan yang sangat kuat terhadap Program Studi Matematika!")
            elif 40 <= skor < 70:
                st.write("Anda memiliki ketertarikan yang moderat terhadap Program Studi Matematika.")
            else:
                st.write("Ketertarikan Anda terhadap Program Studi Matematika relatif rendah.")

    if __name__ == "__main__":
        halaman_utama()

elif page == "Pengantar Matematika":
    st.title("Pengantar Program Studi Matematika")
    st.image("ai.jpg", width=700, caption="Matematika dalam AI")
    st.write("""
        Kalian tau hal-hal yang lagi tren saat ini? AI, Machine Learning, dan hal-hal sejenisnya?
        Semua itu terdiri dari satu fondasi besar, yakni **Matematika**. **Matematika** sendiri tidak hanya
        tentang mengitung, mengerjakan soal, lalu tinggalkan, bukan seperti itu. **Matematika** sendiri memiliki
        banyak sekali penerapannya di seluruh sendi-sendi kehidupan kita. 
        
        Di Program Studi Matematika, mahasiswa tidak hanya mengajarkan tentang teori (bisa kalau mau dikatakan rumus), tetapi juga
        penerapannya di berbagai bidang, termasuk dalam ilmu terapan yang ada saat ini seperti statistika, komputasi, lingkungan, bahkan kalian bisa menjadi dukun loh. Nanti akan dijelaskan di bagian halaman utama 
        Ini juga karena matematika merupakan dasar dari banyak teknologi dan aplikasi dalam kehidupan sehari-hari.
        
        ### Apa benar Matematika hanya berhitung dan berhitung doang isinya?
        Ngga sama sekali. Bahkan, bagi teman-teman yang merasa minder dalan berhitung, jangan khawatir.
        Di program studi Matematika ITK, mahasiswa tidak hanya diajarkan untuk berhitung saja selayaknya
        di SMA, tetapi mahasiswanya juga diajarkan untuk berpikir kritis dan bisa membuktikan bagaimana
        sebuah permasalahan diselesaikan. Tidak hanya itu, nantinya mahasiswa Matematika ITK juga dapat mendalami
        peminatan yang ada, bahkan termasuk **AI** dan **Lingkungan** yang lagi perbincangan hangat di dunia
        saat ini.
        
        ### Berapa kuota yang tersedia di Program studi Matematika ITK?
        Program Studi Matematika ITK menyediakan daya tampung sebesar **40 kursi** untuk jalur **SNBP** dan **35 Kursi**
        untuk **SNBT** saat ini. Sudah pada eligible kan? Fun fact aja, sampai saat ini, Matematika ITK merupakan program studi dengan
        peminat paling sedikit pertama untuk SNBP dan paling sedikit ke-2 untuk SNBT di ITK, yakni sebanyak **19 orang** di SNBP dan **15 orang** di SNBT. (source: https://snpmb.bppp.kemdikbud.go.id/snbp/daftar-ptn-snbp dan https://snpmb.bppp.kemdikbud.go.id/utbk-snbt/daftar-ptn-snbt)

    """)




