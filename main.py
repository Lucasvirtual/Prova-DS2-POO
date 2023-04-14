from controllers.ProdutoController import ProdutoController

app = True
while app:
    app = ProdutoController.exibir_menu()
    if app == False:
        print('\n\n\n\nO programa será finalizado')