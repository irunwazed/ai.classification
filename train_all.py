from libs import helpers, llm, class_jenis
from libs import ner


# training NER
def training_ner():
  text = """
  <div class="wpb_wrapper">
        <p>Prof. Dr. Zudan Arif Fakrulloh, SH., M.H lahir pada tahun 1969 di Sleman, Daerah Istimewa Yogyakarta. Zudan mendapatkan gelar S1 Hukum di Universitas Sebelas Maret pada tahun 1992, kemudian melanjutkan studi S2 pada jurusan Ilmu Hukum di Universitas Diponegoro serta lulus pada tahun 1995. Setelah itu melanjutkan studi S3 Doktor Ilmu Hukum di universitas yang sama dan mendapatkan gelar Doktor Ilmu Hukum pada tahun 2001.</p>
  <p>Zudan mengawali kariernya di pemerintahan pada tahun 1999 yaitu menjadi CPNS di Badan Diklat Kementerian Dalam Negeri. Selang beberapa tahun setelah menjadi PNS, Ia mendapat kepercayaan untuk menjabat sebagai Kasubid Kader PD Bid. Kader Profesionalisme Kediklatan Pusdiklat Kader &amp; Pengemb. Kepemimp. Bandiklat, kemudian naik dan mendapat kepercayaan sebagai Kabag. Penyusunan Rancangan Peraturan Perundang-undangan pada Biro Hukum Sekretaris Jenderal Kementerian Dalam Negeri.</p>
  <p>Seiring berjalannya waktu, Zudan mengemban beberapa jabatan penting di lingkungan Kementerian Dalam Negeri baik untuk jabatan JPT Pratama maupun JPT Madya, seperti Kepala Biro Hukum Pada Sekretariat Jenderal, Staf Ahli Bidang Hukum, Politik dan Hubungan Antar Lembaga Pada Sekretariat Jenderal Kementerian Dalam Negeri, Direktur Jenderal Kependudukan dan Pencatatan Sipil pada Kementerian Dalam Negeri dan terakhir pada jabatan Sekretaris Badan Nasional Pengelola Perbatasan pada Kementerian Dalam Negeri. Selain jabatan struktural di lingkungan Kementerian Dalam Negeri, Zudan juga pernah ditunjuk untuk mengisi beberapa jabatan di luar tugas utamanya sebagai PNS yaitu sebagai Penjabat Gubernur di Provinsi Gorantalo, Provinsi Sulawesi Barat dan terakhir di Provinsi Sulawesi Selatan.</p>
  <p>Selain aktif di pemerintahan, Zudan juga aktif sebagai dosen di beberapa universitas baik negeri maupun swasta, di antaranya dengan menjadi dosen S2 Ilmu Hukum STIH Iblam Jakarta, dosen S2 Ilmu Hukum Universitas Tanjung Pura Pontianak, dosen Magister Manajemen STIE STIEKUBANK Semarang, dosen S2 dan S3 Ilmu Hukum Untag Surabaya, dosen S2 Ilmu Hukum Universitas Borobudur Jakarta, dosen S3 Ilmu Hukum Undip dan beberapa universitas lainnya.</p>
  <p>Pada bulan Januari 2025, Presiden Prabowo Subianto menunjuk Zudan sebagai Kepala BKN berdasarkan Keputusan Presiden Nomor 188/TPA Tahun 2024 tentang Pengangkatan Pejabat Pimpinan Tinggi Utama di Lingkungan Badan Kepegawaian Negara (BKN). Ia resmi menjabat Kepala Badan Kepegawaian Negara sejak 07 Januari 2025.</p>
      </div>
  """
  text = helpers.clean_html(text)
  ner.training(text)
  res = ner.search_entities("Zudan mengemban beberapa jabatan penting di lingkungan Kementerian Dalam Negeri baik")
  print("res", res)

# training_ner()

# ner.training_lib()

def training_jenis():
  class_jenis.training("datasets/datasets_jenis.json")

  res = class_jenis.check_class(["siapa kamu ini?"])
  print("res", res)
  res = class_jenis.check_class_once("siapa kamu ini?")
  print("res", res)

def testing_llm():
  # llm.chat_with_ollama()
  res = llm.ollama_chat("halo")
  print("res", res)

# testing_llm()

