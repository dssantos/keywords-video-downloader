# Keywords Video Downloader
Baixe vídeos do youtube informando apenas algumas palavras

## Como usar

1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv
4. Instale as dependências
5. Coloque as sua palavras-chave no arquivo keywords.txt
6. Execute o aplicativo
7. O videos são salvos na pasta downloads

```console
git clone https://github.com/dssantos/keywords-video-downloader.git
cd keywords_video_downloader
python -m venv .keywords_video_downloader
source .keywords_video_downloader/bin/activate
pip install -r requirements.txt
echo "instalar python no linux\n primeiro programa em python" > keywords.txt
python main.py
ls downloads
```