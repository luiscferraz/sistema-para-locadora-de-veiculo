# -*- coding: latin-1 -*-
#Boa:Frame:frmCliente

import wx
import wx.lib.buttons
import wx.lib.masked.textctrl

#para funcionar no Boa tem que comentar esta parte
from negocio.Cliente import *
from db.ClienteDAO import *
from wx.tools.Editra.src.ebmlib.miscutil import Singleton
#comentar até a linha acima


def create(parent):
    return frmCliente(parent)

[wxID_FRMCLIENTE, wxID_FRMCLIENTEBTNAUALIZAR, wxID_FRMCLIENTEBTNCANCELAR, 
 wxID_FRMCLIENTEBTNEDITAR, wxID_FRMCLIENTEBTNEXCLUIR, 
 wxID_FRMCLIENTEBTNINCLUIR, wxID_FRMCLIENTEBTNPESQUISAR, 
 wxID_FRMCLIENTELSTCLIENTES, wxID_FRMCLIENTELSTESTADOS, 
 wxID_FRMCLIENTEPNLCLIENTE, wxID_FRMCLIENTESTBAIRRO, wxID_FRMCLIENTESTCEP, 
 wxID_FRMCLIENTESTCIDADE, wxID_FRMCLIENTESTCLIENTE, wxID_FRMCLIENTESTCPF, 
 wxID_FRMCLIENTESTEMAIL, wxID_FRMCLIENTESTENDERECO, wxID_FRMCLIENTESTNOME, 
 wxID_FRMCLIENTESTPESQUISA, wxID_FRMCLIENTESTTELEFONE, wxID_FRMCLIENTESTUF, 
 wxID_FRMCLIENTETXTBAIRRO, wxID_FRMCLIENTETXTCEP, wxID_FRMCLIENTETXTCIDADE, 
 wxID_FRMCLIENTETXTCPF, wxID_FRMCLIENTETXTEMAIL, wxID_FRMCLIENTETXTENDERECO, 
 wxID_FRMCLIENTETXTNOME, wxID_FRMCLIENTETXTPESQUISA, 
 wxID_FRMCLIENTETXTTELEFONE, 
] = [wx.NewId() for _init_ctrls in range(30)]

class frmCliente(wx.Frame):
    #Luís explicou que é para que não abra mais de uma página de cliente.
    __metaclass__ = Singleton
    def _init_coll_lstClientes_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='CPF',
              width=130)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Nome',
              width=190)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Telefone', width=120)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='E-mail',
              width=210)
    
    def _init_coll_lstResultado_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='CPF',
              width=130)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Nome',
              width=190)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Telefone', width=120)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='E-mail',
              width=210)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMCLIENTE, name=u'frmCliente',
              parent=prnt, pos=wx.Point(430, 98), size=wx.Size(641, 526),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Cliente')
        self.SetClientSize(wx.Size(825, 488))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlCliente = wx.Panel(id=wxID_FRMCLIENTEPNLCLIENTE,
              name=u'pnlCliente', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(625, 488), style=wx.TAB_TRAVERSAL)

        self.stCliente = wx.StaticBox(id=wxID_FRMCLIENTESTCLIENTE,
              label=u'Dados Pessoais', name=u'stCliente',
              parent=self.pnlCliente, pos=wx.Point(128, 8), size=wx.Size(688,
              232), style=0)

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTCPF,
              name=u'txtCpf', parent=self.pnlCliente, pos=wx.Point(144, 56),
              size=wx.Size(152, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)
        self.txtCpf.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.stCpf = wx.StaticText(id=wxID_FRMCLIENTESTCPF, label=u'CPF :',
              name=u'stCpf', parent=self.pnlCliente, pos=wx.Point(144, 40),
              size=wx.Size(27, 13), style=0)

        self.stNome = wx.StaticText(id=wxID_FRMCLIENTESTNOME, label=u'Nome :',
              name=u'stNome', parent=self.pnlCliente, pos=wx.Point(320, 40),
              size=wx.Size(35, 13), style=0)

        self.txtNome = wx.TextCtrl(id=wxID_FRMCLIENTETXTNOME, name=u'txtNome',
              parent=self.pnlCliente, pos=wx.Point(320, 56), size=wx.Size(480,
              21), style=0, value=u'')

        self.txtEndereco = wx.TextCtrl(id=wxID_FRMCLIENTETXTENDERECO,
              name=u'txtEndereco', parent=self.pnlCliente, pos=wx.Point(144,
              104), size=wx.Size(390, 21), style=0, value=u'')

        self.stEndereco = wx.StaticText(id=wxID_FRMCLIENTESTENDERECO,
              label=u'Endere\xe7o :', name=u'stEndereco',
              parent=self.pnlCliente, pos=wx.Point(144, 88), size=wx.Size(53,
              13), style=0)

        self.txtBairro = wx.TextCtrl(id=wxID_FRMCLIENTETXTBAIRRO,
              name=u'txtBairro', parent=self.pnlCliente, pos=wx.Point(560, 104),
              size=wx.Size(242, 21), style=0, value=u'')

        self.stBairro = wx.StaticText(id=wxID_FRMCLIENTESTBAIRRO,
              label=u'Bairro :', name=u'stBairro', parent=self.pnlCliente,
              pos=wx.Point(560, 88), size=wx.Size(36, 13), style=0)

        self.stCidade = wx.StaticText(id=wxID_FRMCLIENTESTCIDADE,
              label=u'Cidade :', name=u'stCidade', parent=self.pnlCliente,
              pos=wx.Point(144, 136), size=wx.Size(61, 13), style=0)

        self.txtCidade = wx.TextCtrl(id=wxID_FRMCLIENTETXTCIDADE,
              name=u'txtCidade', parent=self.pnlCliente, pos=wx.Point(144, 152),
              size=wx.Size(390, 21), style=0, value=u'')

        self.txtCep = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTCEP,
              name=u'txtCep', parent=self.pnlCliente, pos=wx.Point(560, 152),
              size=wx.Size(152, 21), style=0, value=u'  .   -   ')
        self.txtCep.SetAutoformat('')
        self.txtCep.SetMask(u'XX.XXX-XXX')
        self.txtCep.SetDatestyle('MDY')
        self.txtCep.SetFormatcodes('')
        self.txtCep.SetDescription('')
        self.txtCep.SetExcludeChars('')
        self.txtCep.SetValidRegex('')
        self.txtCep.SetMaxLength(10)
        self.txtCep.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.txtCep.SetInsertionPoint(9)
        
        self.listaEstados = ["AC", "AL", "AP", "AM", "BA", "CE",
              "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE",
              "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        
        self.lstEstados = wx.Choice(choices= self.listaEstados,
              id=wxID_FRMCLIENTELSTESTADOS, name=u'lstEstados',
              parent=self.pnlCliente, pos=wx.Point(736, 152), size=wx.Size(64,
              21), style=0)
        self.lstEstados.Bind(wx.EVT_CHOICE, self.OnLstEstadosChoice,
              id=wxID_FRMCLIENTELSTESTADOS)

        self.stUf = wx.StaticText(id=wxID_FRMCLIENTESTUF, label=u'UF :',
              name=u'stUf', parent=self.pnlCliente, pos=wx.Point(736, 136),
              size=wx.Size(21, 13), style=0)

        self.stTelefone = wx.StaticText(id=wxID_FRMCLIENTESTTELEFONE,
              label=u'Telefone :', name=u'stTelefone', parent=self.pnlCliente,
              pos=wx.Point(144, 184), size=wx.Size(50, 13), style=0)

        self.txtTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTTELEFONE,
              name=u'txtTelefone', parent=self.pnlCliente, pos=wx.Point(144,
              200), size=wx.Size(208, 21), style=0, value='')
        self.txtTelefone.SetAutoformat('')
        self.txtTelefone.SetMask(u'+55 ( XX ) XXXX-XXXX')
        self.txtTelefone.SetDatestyle('MDY')
        self.txtTelefone.SetFormatcodes('')
        self.txtTelefone.SetDescription('')
        self.txtTelefone.SetExcludeChars('')
        self.txtTelefone.SetValidRegex('')
        self.txtTelefone.SetMaxLength(20)
        self.txtTelefone.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.txtEmail = wx.TextCtrl(id=wxID_FRMCLIENTETXTEMAIL,
              name=u'txtEmail', parent=self.pnlCliente, pos=wx.Point(376, 200),
              size=wx.Size(424, 21), style=0, value=u'')

        self.txtPesquisa = wx.TextCtrl(id=wxID_FRMCLIENTETXTPESQUISA,
              name=u'txtPesquisa', parent=self.pnlCliente, pos=wx.Point(144,
              288), size=wx.Size(400, 21), style=0, value=u'')

        self.btnPesquisar = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMCLIENTEBTNPESQUISAR,
              name=u'btnPesquisar', parent=self.pnlCliente, pos=wx.Point(568,
              280), size=wx.Size(31, 32), style=0)
        self.btnPesquisar.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarButton,
              id=wxID_FRMCLIENTEBTNPESQUISAR)

        self.stEmail = wx.StaticText(id=wxID_FRMCLIENTESTEMAIL,
              label=u'E-mail :', name=u'stEmail', parent=self.pnlCliente,
              pos=wx.Point(376, 184), size=wx.Size(36, 13), style=0)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNINCLUIR,
              label=u'Incluir', name=u'btnIncluir', parent=self.pnlCliente,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMCLIENTEBTNINCLUIR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlCliente,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)
        self.btnEditar.Bind(wx.EVT_BUTTON, self.OnBtnEditarButton,
              id=wxID_FRMCLIENTEBTNEDITAR)

        self.btnAualizar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNAUALIZAR,
              label=u'Atualizar', name=u'btnAualizar', parent=self.pnlCliente,
              pos=wx.Point(24, 312), size=wx.Size(76, 25), style=0)
        self.btnAualizar.Bind(wx.EVT_BUTTON, self.OnBtnAualizarButton,
              id=wxID_FRMCLIENTEBTNAUALIZAR)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlCliente,
              pos=wx.Point(24, 360), size=wx.Size(76, 25), style=0)
        self.btnExcluir.Bind(wx.EVT_BUTTON, self.OnBtnExcluirButton,
              id=wxID_FRMCLIENTEBTNEXCLUIR)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlCliente,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMCLIENTEBTNCANCELAR)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMCLIENTESTPESQUISA,
              label=u'Pesquisa por CPF', name=u'stPesquisa',
              parent=self.pnlCliente, pos=wx.Point(128, 256), size=wx.Size(688,
              224), style=0)
        
        #Para funcionar no boa o comentário começa nesta linha
##        self.lstClientes = wx.ListCtrl(id=wxID_FRMCLIENTELSTCLIENTES,
##              name=u'lstClientes', parent=self.pnlCliente, pos=wx.Point(144,
##              328), size=wx.Size(656, 128), style=wx.LC_REPORT)
##        self._init_coll_lstClientes_Columns(self.lstClientes)
        #Para funcionar no boa o comentário termina nesta linha
        
        
        self.stCep = wx.StaticText(id=wxID_FRMCLIENTESTCEP, label=u'CEP :',
              name=u'stCep', parent=self.pnlCliente, pos=wx.Point(560, 136),
              size=wx.Size(27, 13), style=0)
        
        #precisa ser comentado para funcionar no boa
        self.gerarListctrl(self)
        self.btnAualizar.Disable()
        
    
    #método responsável pela gerarListctrl
    #Para funcionar no Boa tem que comentar todo esse método
    def gerarListctrl(self,event):
        self.lstClientes = wx.ListCtrl(id=wxID_FRMCLIENTELSTCLIENTES,
              name=u'lstClientes', parent=self.pnlCliente, pos=wx.Point(144,
              328), size=wx.Size(656, 128), style=wx.LC_REPORT)
        self._init_coll_lstClientes_Columns(self.lstClientes)
        
        self.inserirInformacoesNaListctrl(self.lstClientes)
        
        return self.lstClientes
              

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnLstEstadosChoice(self, event):
        event.Skip()
    
    def getEstado(self,uf):
        #Método feito para colocar todos os tipos
        
        posicao = 0
        for j in self.listaEstados:            
            if j==uf:
                #print j
                #print posicao
                return posicao
            posicao = posicao + 1  
    
    def clearTextfield(self):
        #Método responsável por limpar os campos
        self.txtCpf.Clear()
        self.txtNome.Clear()
        self.txtEndereco.Clear()
        self.txtTelefone.Clear()
        self.txtCep.Clear()
        self.txtBairro.Clear()
        self.txtCidade.Clear()
        self.txtEmail.Clear()
        
        self.lstEstados.Select(-1)
        
    def obterDadosInformados(self):
        #Método para obter os dados fornecidos
        cpf = self.txtCpf.GetValue()
        nome = self.txtNome.GetValue()
        endereco = self.txtEndereco.GetValue()
        telefone = self.txtTelefone.GetValue()
        cep = self.txtCep.GetValue()
        bairro = self.txtBairro.GetValue()
        cidade = self.txtCidade.GetValue()
        email = self.txtEmail.GetValue()        
        uf = self.lstEstados.GetStringSelection()
        
        #a lista será usada posteriormente na ação do botão de incluir um cliente
        lista = [cpf,nome,endereco,telefone,cep,bairro,cidade,uf,email]
        
        return lista
    
    def updateListctrl(self):
        #Método responsável por atualizar a listctrl após inserir,deletar e atualizar um cliente.
        self.lstClientes.Destroy()
        self.gerarListctrl(self)
        
    def inserirInformacoesNaListctrl(self,lista):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        dao = ClienteDAO()
        #Pega todos os clientes presentes no banco de dados
        rows = dao.getAllClientes()
        if rows:
            for row in rows:
                num_itens = lista.GetItemCount()
                lista.InsertStringItem(num_itens,str(row[1]))
                #Vai na coluna correspondente da Listctrl e coloca a coluna correspondete
                #do banco de dados. 
                lista.SetStringItem(num_itens,1,row[2])
                lista.SetStringItem(num_itens,2,row[4])
                lista.SetStringItem(num_itens,3,row[9])
    
    def inserirResultadoDeBusca(self,lista,cpf):
        dao = ClienteDAO()
        clienteEncontrado = dao.procurarCliente(cpf)
        #print clienteEncontrado.toString()
        num_itens = lista.GetItemCount()
        lista.InsertStringItem(num_itens,str(clienteEncontrado.getCpf()))
        lista.SetStringItem(num_itens,1,clienteEncontrado.getNome())
        lista.SetStringItem(num_itens,2,clienteEncontrado.getTelefone())
        lista.SetStringItem(num_itens,3,clienteEncontrado.getTelefone())
     
    def OnBtnIncluirButton(self, event):
        #Método que inclui um Cliente no banco de dados.                
        try:
            lista = self.obterDadosInformados()
            cliente = Cliente(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]) 
                                        
            dao = ClienteDAO()
            dao.insertCliente(cliente)
            
            self.updateListctrl()
            
            self.clearTextfield()
        except:
            print "Erro ao salvar no banco."

    def OnBtnCancelarButton(self, event):
        self.clearTextfield()
        
        #Habilitando os botões outra vez caso o botão cancelar seja usado na edição.
        self.txtCpf.Enable()
        self.btnIncluir.Enable()
        self.btnExcluir.Enable()
        self.btnEditar.Enable()
        self.btnAualizar.Disable()
        
        #volta a não apresentar nada na lista de estados
        self.lstEstados.Select(-1)
        
        #Caso seja feita usado após alguma pesquisa
        self.btnPesquisar.Enable()
        self.txtPesquisa.Clear()
        
    def OnBtnEditarButton(self, event):
        #Método para editar um cliente selecionado na Listctrl
        
        dao = ClienteDAO()
        
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstClientes.GetFocusedItem()
        
        #desabilitando os botões desnecessários
        self.btnAualizar.Enable()
        self.btnIncluir.Disable()
        self.btnExcluir.Disable()
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            cpf = self.lstClientes.GetItemText(indice)
            
            #busca o cliente selecionado no banco de dados         
            clienteSelecionado = dao.procurarCliente(cpf)
            
            #Colocando os valores do banco nos campos da tela
            self.txtCpf.SetValue(str(clienteSelecionado.getCpf()))
            #O CPF não pode ser editado
            self.txtCpf.Disable()               
            self.txtNome.SetValue(clienteSelecionado.getNome())
            self.txtEndereco.SetValue(clienteSelecionado.getEndereco())
            self.txtBairro.SetValue(clienteSelecionado.getBairro())
            self.txtCidade.SetValue(clienteSelecionado.getCidade())
            self.txtCep.SetValue(clienteSelecionado.getCep())
            self.lstEstados.SetLabel(clienteSelecionado.getUf())                          
            self.txtTelefone.SetValue(clienteSelecionado.getTelefone())
            self.txtEmail.SetValue(clienteSelecionado.getEmail()) 
            self.lstEstados.Select(self.getEstado(clienteSelecionado.getUf()))    
            
            self.btnEditar.Disable()       
                        
        else:            
            dlg = wx.MessageDialog(self,'Selecione um cliente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            #Voltando o estado dos botões
            self.btnAualizar.Disable()
            self.btnIncluir.Enable()
            self.btnExcluir.Enable()
        
        

    def OnBtnAualizarButton(self, event):
        #Método para atualizar cliente
        
        #obtendo informações dos campos da tela  
        lista = self.obterDadosInformados()
        #guardando informações em um cliente
        cliente = Cliente(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]) 
        
        dao = ClienteDAO()
        #atualizando um cliente no banco de dados
        dao.updateCliente(cliente)
        
        #atualiza a Listctrl
        self.updateListctrl()
        
        #limpando os campos
        self.clearTextfield()
                
        #retornando o estado incial dos botões
        self.txtCpf.Enable()
        self.btnExcluir.Enable()
        self.btnIncluir.Enable()
        self.btnEditar.Enable()
        self.btnAualizar.Disable()
        
        

    def OnBtnExcluirButton(self, event):       
                
        dao = ClienteDAO()
        
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstClientes.GetFocusedItem()
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1:
            cpf = self.lstClientes.GetItemText(indice)
            try:                
                #deleta o cliente do banco
                dao.deleteCliente(cpf)
                #para atualizar a Listctrl retirando o cliente q existia nela
                self.updateListctrl()                
            except:
                #caso o cliente não seja removido, uma caixa de diálogo será mostrada
                caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Selecione um cliente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
         


    def OnBtnPesquisarButton(self, event):
        cpf = self.txtPesquisa.GetValue()
        
        dao = ClienteDAO()
        try:
            clienteSelecionado  = dao.procurarCliente(cpf)
            self.txtCpf.SetValue(clienteSelecionado.getCpf())
            self.txtNome.SetValue(clienteSelecionado.getNome())
            self.txtEndereco.SetValue(clienteSelecionado.getEndereco())
            self.txtBairro.SetValue(clienteSelecionado.getBairro())
            self.txtCidade.SetValue(clienteSelecionado.getCidade())
            self.txtCep.SetValue(clienteSelecionado.getCep())
            self.lstEstados.SetLabel(clienteSelecionado.getUf())                          
            self.txtTelefone.SetValue(clienteSelecionado.getTelefone())
            self.txtEmail.SetValue(clienteSelecionado.getEmail()) 
            self.lstEstados.Select(self.getEstado(clienteSelecionado.getUf()))
            
            self.btnAualizar.Disable()
            self.btnIncluir.Disable()
            self.btnEditar.Disable()
            self.btnExcluir.Disable()
            self.btnPesquisar.Disable()
            
            
        except:
            caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtPesquisa.Clear()
        
        
    
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
