import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyautogui
import time
import webbrowser
import datetime
import wikipedia

# Inicializa o reconhecedor de áudio e o mecanismo de voz
audio = sr.Recognizer()
ia = pyttsx3.init()

def executar_comandos(prompt=None):
    """Captura o comando de voz do usuário."""
    try:
        with sr.Microphone() as source:
            if prompt:
                ia.say(prompt)
                ia.runAndWait()
            
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'alexsander' in comando:
                comando = comando.replace('alexsander', '')
            return comando
    except:
        print("Microfone não está funcionando")
        return ""

def enviar_mensagem_whatsapp():
    """Envia uma mensagem pelo WhatsApp após perguntar para quem e o conteúdo."""
    contato = executar_comandos("Para quem você deseja enviar a mensagem?")
    
    if contato:
        mensagem = executar_comandos(f"O que você deseja enviar para {contato}?")
        
        if mensagem:
            ia.say(f"Enviando mensagem para {contato}")
            ia.runAndWait()

            # Abre o WhatsApp Web
            webbrowser.open("https://web.whatsapp.com")
            time.sleep(10)  # Espera o WhatsApp Web carregar

            # Localiza a barra de pesquisa e insere o nome do contato
            pyautogui.click(x=200, y=200)  # Ajuste as coordenadas conforme necessário
            pyautogui.write(contato)
            time.sleep(2)  # Espera carregar os resultados

            # Pressiona Enter para abrir a conversa com o contato
            pyautogui.press('enter')
            time.sleep(2)

            # Digita a mensagem e envia
            pyautogui.write(mensagem)
            pyautogui.press('enter')
            ia.say(f"Mensagem para {contato} foi enviada")
            ia.runAndWait()
        else:
            ia.say("Não foi possível capturar a mensagem")
            ia.runAndWait()
    else:
        ia.say("Não foi possível capturar o nome do contato")
        ia.runAndWait()

def voz_usuario():
    """Interpreta e executa os comandos de voz."""
    comando = executar_comandos()
    
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        ia.say(f'Agora são {hora}')
        ia.runAndWait()
    
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        ia.say(f'{resultado}')
        ia.runAndWait()
    
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        ia.say('Tocando música')
        ia.runAndWait()
    
    elif 'abra a máquina' in comando:
        ia.say("Abrindo máquina de combate")
        ia.runAndWait()
        webbrowser.open("https://www.youtube.com")
        webbrowser.open("https://www.instagram.com")
        webbrowser.open("https://github.com")
    
    elif 'enviar mensagem' in comando:
        enviar_mensagem_whatsapp()

# Iniciar o assistente
voz_usuario()
