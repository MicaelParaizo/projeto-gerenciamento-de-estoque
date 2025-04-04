import customtkinter
 
def desmarcar_checkbox():
    var_checkbox.set(0)  # Desmarca a checkbox
 
# Configuração da janela
janela = customtkinter.CTk()
janela.title("Exemplo Checkbox")
 
# Variável associada ao checkbox
var_checkbox = customtkinter.IntVar()
 
# Criando o checkbox
checkbox = customtkinter.CTkCheckBox(janela, text="Opção", variable=var_checkbox)
checkbox.pack(pady=10)
 
# Botão para desmarcar
botao = customtkinter.CTkButton(janela, text="Desmarcar", command=desmarcar_checkbox)
botao.pack(pady=10)
 
janela.mainloop()
 