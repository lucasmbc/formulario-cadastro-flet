import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de contato"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def enviar_formulario(e):
        if not campo_nome.value or not campo_email.value or not campo_mensagem.value:
            mensagem.value = "Por favor, preencha todos os campos!"
            mensagem.color = "red"
            page.update()
        else:
            mensagem.value = "Formulário enviado com sucesso!"
            mensagem.color = "green"
            
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""

        page.update()

    
    campo_nome = ft.TextField(label="Nome", width=300)
    campo_email = ft.TextField(label="Email", width=300)
    campo_mensagem = ft.TextField(label="Mensagem", multiline=True, width=300, height=100)

    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    mensagem = ft.Text()

    layout = ft.Column(
            controls=[
                ft.Text("Formulário de Contato", size=24, weight="bold"),
                campo_nome,
                campo_email,
                campo_mensagem,
                botao_enviar,
                mensagem,
            ],
            alignment="center",
            horizontal_alignment="center",

    )

    page.add(layout)

ft.app(target=main)
