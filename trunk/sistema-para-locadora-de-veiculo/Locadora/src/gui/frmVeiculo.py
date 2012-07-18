# -*- coding: latin-1 -*-
#Boa:Frame:frmVeiculo

import wx
import wx.lib.buttons
import wx.lib.masked.textctrl
from db.TipoVeiculoDAO import *
from negocio.Veiculo import *
from db.VeiculoDAO import *
from db.VeiculoDAO import VeiculoDAO
from negocio.Veiculo import *
from wx.tools.Editra.src.ebmlib.miscutil import Singleton

def create(parent):
    
    return frmVeiculo(parent)

[wxID_FRMVEICULO, wxID_FRMVEICULOBTNATUALIZAR, wxID_FRMVEICULOBTNCANCELAR, 
 wxID_FRMVEICULOBTNEDITAR, wxID_FRMVEICULOBTNEXCLUIR, 
 wxID_FRMVEICULOBTNINCLUIR, wxID_FRMVEICULOBTNPESQUISAR, 
 wxID_FRMVEICULOLSTTIPO, wxID_FRMVEICULOLSTVEICULOS, 
 wxID_FRMVEICULOPNLVEICULO, wxID_FRMVEICULOSTCOR, wxID_FRMVEICULOSTMARCA, 
 wxID_FRMVEICULOSTMODELO, wxID_FRMVEICULOSTPESQUISA, wxID_FRMVEICULOSTPLACA, 
 wxID_FRMVEICULOSTQUILOMETRAGEM, wxID_FRMVEICULOSTTIPO, 
 wxID_FRMVEICULOSTVEICULO, wxID_FRMVEICULOTXTCOR, wxID_FRMVEICULOTXTMARCA, 
 wxID_FRMVEICULOTXTMODELO, wxID_FRMVEICULOTXTPESQUISA, 
 wxID_FRMVEICULOTXTPLACA, wxID_FRMVEICULOTXTQUILOMETRAGEMATUAL, 
] = [wx.NewId() for _init_ctrls in range(24)]

class frmVeiculo(wx.Frame):
    #Luís explicou que é para que não abra mais de uma página de cliente.
    __metaclass__ = Singleton
    def _init_coll_lstVeiculos_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Placa',
              width=80)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Marca',
              width=120)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Modelo',
              width=150)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Cor',
              width=120)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Disponibilidade', width=110)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading='Cod. do tipo ', width=90)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT,
              heading='Km Atual', width=68)
        
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMVEICULO, name='frmVeiculo',
              parent=prnt, pos=wx.Point(350, 28), size=wx.Size(967, 526),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Ve\xedculos')
        self.SetClientSize(wx.Size(951, 488))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlVeiculo = wx.Panel(id=wxID_FRMVEICULOPNLVEICULO,
              name=u'pnlVeiculo', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(951, 488), style=wx.TAB_TRAVERSAL)

        self.stVeiculo = wx.StaticBox(id=wxID_FRMVEICULOSTVEICULO,
              label=u'Dados do Ve\xedculo', name=u'stVeiculo',
              parent=self.pnlVeiculo, pos=wx.Point(128, 8), size=wx.Size(800,
              144), style=0)

        self.stPlaca = wx.StaticText(id=wxID_FRMVEICULOSTPLACA,
              label=u'Placa :', name=u'stPlaca', parent=self.pnlVeiculo,
              pos=wx.Point(144, 40), size=wx.Size(33, 13), style=0)
        self.stPlaca.SetToolTipString(u'stCpf')

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMVEICULOTXTPLACA,
              name=u'txtPlaca', parent=self.pnlVeiculo, pos=wx.Point(144, 56),
              size=wx.Size(104, 21), style=0, value='')
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.stMarca = wx.StaticText(id=wxID_FRMVEICULOSTMARCA,
              label=u'Marca :', name=u'stMarca', parent=self.pnlVeiculo,
              pos=wx.Point(264, 40), size=wx.Size(37, 13), style=0)

        self.txtMarca = wx.TextCtrl(id=wxID_FRMVEICULOTXTMARCA,
              name=u'txtMarca', parent=self.pnlVeiculo, pos=wx.Point(264, 56),
              size=wx.Size(292, 21), style=0, value=u'')

        self.txtModelo = wx.TextCtrl(id=wxID_FRMVEICULOTXTMODELO,
              name=u'txtModelo', parent=self.pnlVeiculo, pos=wx.Point(572, 56),
              size=wx.Size(338, 21), style=0, value=u'')

        self.stModelo = wx.StaticText(id=wxID_FRMVEICULOSTMODELO,
              label=u'Modelo :', name=u'stModelo', parent=self.pnlVeiculo,
              pos=wx.Point(572, 40), size=wx.Size(42, 13), style=0)

        self.stQuilometragem = wx.StaticText(id=wxID_FRMVEICULOSTQUILOMETRAGEM,
              label='Quilometragem atual :', name='stQuilometragem',
              parent=self.pnlVeiculo, pos=wx.Point(144, 88), size=wx.Size(107,
              13), style=0)

        self.txtQuilometragemAtual = wx.TextCtrl(id=wxID_FRMVEICULOTXTQUILOMETRAGEMATUAL,
              name='txtQuilometragemAtual', parent=self.pnlVeiculo,
              pos=wx.Point(144, 104), size=wx.Size(104, 21), style=0, value='')

        self.txtCor = wx.TextCtrl(id=wxID_FRMVEICULOTXTCOR, name=u'txtCor',
              parent=self.pnlVeiculo, pos=wx.Point(264, 104), size=wx.Size(292,
              21), style=0, value=u'')

        self.stCor = wx.StaticText(id=wxID_FRMVEICULOSTCOR, label=u'Cor :',
              name=u'stCor', parent=self.pnlVeiculo, pos=wx.Point(264, 88),
              size=wx.Size(25, 13), style=0)

        self.stTipo = wx.StaticText(id=wxID_FRMVEICULOSTTIPO,
              label=u'Tipo de Veículo :', name=u'stTipo',
              parent=self.pnlVeiculo, pos=wx.Point(572, 88), size=wx.Size(90,
              13), style=0)

        self.lstTipo = wx.Choice(choices=TipoVeiculoDAO.listarTiposDeVeiculos(), id=wxID_FRMVEICULOLSTTIPO,
              name=u'lstTipo', parent=self.pnlVeiculo, pos=wx.Point(572, 104),
              size=wx.Size(338, 21), style=0)
        self.lstTipo.Bind(wx.EVT_CHOICE, self.getIdTipo,
              id=wxID_FRMVEICULOLSTTIPO)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMVEICULOSTPESQUISA,
              label=u'Pesquisa por Placa', name=u'stPesquisa',
              parent=self.pnlVeiculo, pos=wx.Point(128, 168), size=wx.Size(800,
              312), style=0)

        self.txtPesquisa = wx.TextCtrl(id=wxID_FRMVEICULOTXTPESQUISA,
              name=u'txtPesquisa', parent=self.pnlVeiculo, pos=wx.Point(144,
              200), size=wx.Size(400, 21), style=0, value=u'')

        self.btnPesquisar = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMVEICULOBTNPESQUISAR,
              name=u'btnPesquisar', parent=self.pnlVeiculo, pos=wx.Point(568,
              192), size=wx.Size(31, 32), style=0)
        self.btnPesquisar.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarButton,
              id=wxID_FRMVEICULOBTNPESQUISAR)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNINCLUIR,
              label=u'Incluir', name=u'btnIncluir', parent=self.pnlVeiculo,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMVEICULOBTNINCLUIR)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMVEICULOSTPESQUISA,
              label=u'Pesquisa por Placa', name=u'stPesquisa',
              parent=self.pnlVeiculo, pos=wx.Point(128, 168), size=wx.Size(800,
              312), style=0)
         #Para funcionar no boa o comentário começa nesta linha
##        self.lstVeiculos = wx.ListCtrl(id=wxID_FRMVEICULOLSTVEICULOS,
##              name=u'lstVeiculos', parent=self.pnlVeiculo, pos=wx.Point(144,
##              240), size=wx.Size(760, 216), style=wx.LC_REPORT)
##        self.lstVeiculos.Show(True)
##        self.lstVeiculos.SetAutoLayout(False)
##        self._init_coll_lstVeiculos_Columns(self.lstVeiculos)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMVEICULOBTNCANCELAR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 184), size=wx.Size(76, 25), style=0)
        self.btnEditar.Bind(wx.EVT_BUTTON, self.OnBtnEditarButton,
              id=wxID_FRMVEICULOBTNEDITAR)

        self.btnAtualizar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNATUALIZAR,
              label=u'Atualizar', name=u'btnAtualizar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 224), size=wx.Size(76, 25), style=0)
        self.btnAtualizar.Bind(wx.EVT_BUTTON, self.OnBtnAtualizarButton,
              id=wxID_FRMVEICULOBTNATUALIZAR)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlVeiculo,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)
        self.btnExcluir.Bind(wx.EVT_BUTTON, self.OnBtnExcluirButton,
              id=wxID_FRMVEICULOBTNEXCLUIR)
        
        #precisa ser comentado para funcionar no boa
        self.gerarListctrl(self)
        
        self.btnAtualizar.Disable()
    
    #método responsável pela gerarListctrl
    #Para funcionar no Boa tem que comentar todo esse método
    def gerarListctrl(self,event):
        
        self.lstVeiculos = wx.ListCtrl(id=wxID_FRMVEICULOLSTVEICULOS,
              name=u'lstVeiculos', parent=self.pnlVeiculo, pos=wx.Point(144,
              240), size=wx.Size(760, 216), style=wx.LC_REPORT)
        self.lstVeiculos.Show(True)
        self.lstVeiculos.SetAutoLayout(False)
        self._init_coll_lstVeiculos_Columns(self.lstVeiculos)
        
        self.inserirInformacoesNaListctrl(self.lstVeiculos)
        
        return self.lstVeiculos

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def getIdTipo(self,event):
        # pega o id do tipo de veículo selecionado
        tipos = TipoVeiculoDAO().getAllTipos()
        for i in tipos:
            if (i[3] == self.lstTipo.GetStringSelection()):
                self.idTipo = i[0]
                #print self.idTipo
                return self.idTipo
            
    def getDescricaoById(self,idTipoVeiculo):
        #Método feito para colocar todos os tipos
        tipos = TipoVeiculoDAO().getAllTipos()
        listaTipos = []
        for i in tipos:
            listaTipos.append(i[0])
        
        posicao = 0
        for j in listaTipos:            
            if j==idTipoVeiculo:
                #print j
                #print posicao
                return posicao
            posicao = posicao + 1    
        
    
    def clearTextfield(self):
        #Método responsável por limpar os campos
        self.txtPlaca.Clear()
        self.txtMarca.Clear()
        self.txtCor.Clear()
        self.txtModelo.Clear()
        self.txtQuilometragemAtual.Clear()
        
        self.lstTipo.Select(-1)
        
        
    def obterDadosInformados(self):
        #Método para obter os dados fornecidos
        placa = str(self.txtPlaca.GetValue())
        #garantindo que ela sempre será salva com letras maiúsculas
        #placaFormatada = placa.upper()
        
        marca = str(self.txtMarca.GetValue())
        cor = str(self.txtCor.GetValue())
        modelo = str(self.txtModelo.GetValue())      
        tipo = frmVeiculo.getIdTipo(self, self.lstTipo)
        quilometragemAtual = self.txtQuilometragemAtual.GetValue()
        
        
        #a lista será usada posteriormente na ação do botão de incluir um veículo
        return [placa.upper(),marca.upper(),cor.upper(),modelo.upper(),tipo,quilometragemAtual]
    
    def updateListctrl(self):
        #Método responsável por atualizar a listctrl após inserir,deletar e atualizar um cliente.
        self.lstVeiculos.Destroy()
        self.gerarListctrl(self)
    
    def inserirInformacoesNaListctrl(self,lista):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega todos os tipos de veículos presentes no banco de dados
        rows = VeiculoDAO.getAllVeiculos()
        if rows:
            for row in rows:
                num_itens = lista.GetItemCount()
                lista.InsertStringItem(num_itens,str(row[1]))
                lista.SetStringItem(num_itens,1,row[2])
                lista.SetStringItem(num_itens,2,row[4])
                lista.SetStringItem(num_itens,3,row[3])
                lista.SetStringItem(num_itens,4,row[5])
                lista.SetStringItem(num_itens,5,str(row[6]))
                lista.SetStringItem(num_itens,6,str(row[7]))

    
    def OnBtnPesquisarButton(self, event):
        placaInformada = str(self.txtPesquisa.GetValue())
        #print placaInformada.upper()
        
        try:
            veiculo = VeiculoDAO.procurarVeiculo(placaInformada.upper())
            idTipoVeiculo = veiculo.getIdTipoVeiculo()
            posicao = self.getDescricaoById(idTipoVeiculo)
            
            self.txtPlaca.SetValue(str(veiculo.getPlaca()))
            self.txtMarca.SetValue (str(veiculo.getMarca()))
            self.txtCor.SetValue (str(veiculo.getCor()))
            self.txtModelo.SetValue (str(veiculo.getModelo()))
            self.txtQuilometragemAtual.SetValue(str(veiculo.getQuilometragemAtual()))
            self.lstTipo.Select(posicao)
            
            self.btnAtualizar.Disable()
            self.btnIncluir.Disable()
            self.btnEditar.Disable()
            self.btnExcluir.Disable()
            self.btnPesquisar.Disable()
        except:
            self.txtPesquisa.Clear()
            
            caixaDeDialogo = wx.MessageDialog(self,'Veículo inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()

    def OnBtnIncluirButton(self, event):
        #Método que inclui um tipo de veículo no banco de dados.                
        try:
            lista = self.obterDadosInformados()
            veiculo = Veiculo(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])                        
            if (veiculo.validarPlaca() is True):
                
                VeiculoDAO.insertVeiculo(veiculo)
                
                self.updateListctrl()
                           
                self.clearTextfield()
            else:
                caixaDeDialogo = wx.MessageDialog(self,'Placa inválida.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
        except:
            #print "Erro ao salvar no banco."
            caixaDeDialogo = wx.MessageDialog(self,'Veículo existente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()

    def OnBtnCancelarButton(self, event):
        self.clearTextfield()
        
        #Habilitando os botões outra vez caso o botão cancelar seja usado na edição.
        self.txtPlaca.Enable()
        self.btnIncluir.Enable()
        self.btnExcluir.Enable()
        self.btnEditar.Enable()
        self.btnAtualizar.Disable()
        
        #Caso seja feita usado após alguma pesquisa
        self.txtPesquisa.Clear()
        self.btnPesquisar.Enable()

    def OnBtnEditarButton(self, event):
        #Método para editar um veículo selecionado na Listctrl
                
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstVeiculos.GetFocusedItem()
        
        #desabilitando os botões desnecessários
        self.btnAtualizar.Enable()
        self.btnIncluir.Disable()
        self.btnExcluir.Disable()
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            placa = self.lstVeiculos.GetItemText(indice)
            #print placa
            
            #busca o veículo selecionado no banco de dados         
            veiculoSelecionado = VeiculoDAO.procurarVeiculo(placa)
            #print veiculoSelecionado.toString()
            idTipoVeiculo = veiculoSelecionado.getIdTipoVeiculo()
            
            #pegando a posição que este id tá no lstTipo
            posicao = self.getDescricaoById(idTipoVeiculo)
            
            #Colocando os valores do banco nos campos da tela
            self.txtPlaca.SetValue(veiculoSelecionado.getPlaca())            
            #A placa não pode ser editada      
            self.txtPlaca.Disable() 
            self.lstTipo.Select(posicao)
            self.txtMarca.SetValue(veiculoSelecionado.getMarca())             
            self.txtModelo.SetValue(veiculoSelecionado.getModelo())
            self.txtQuilometragemAtual.SetValue (str(veiculoSelecionado.getQuilometragemAtual()))
            self.txtCor.SetValue(veiculoSelecionado.getCor())
            self.btnEditar.Disable()
        else:            
            caixaDeMensagem = wx.MessageDialog(self,'Selecione um veículo.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeMensagem.ShowModal()
            caixaDeMensagem.Destroy()
            #Voltando o estado dos botões
            self.btnAtualizar.Disable()
            self.btnIncluir.Enable()
            self.btnExcluir.Enable()

    def OnBtnAtualizarButton(self, event):
        #Método para atualizar tipo
        
        #obtendo informações dos campos da tela  
        lista = self.obterDadosInformados()
        #guardando informações em um veículo
        veiculo = Veiculo(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]) 
        
        #atualizando um veículo no banco de dados
        VeiculoDAO.updateVeiculo(veiculo)
        
        #atualiza a Listctrl
        self.updateListctrl()
        
        #limpando os campos
        self.clearTextfield()
                
        #retornando o estado incial dos botões
        self.txtPlaca.Enable()
        self.btnExcluir.Enable()
        self.btnIncluir.Enable()
        self.btnEditar.Enable()
        self.btnAtualizar.Disable()

    def OnBtnExcluirButton(self, event):
        
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstVeiculos.GetFocusedItem()
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1:
            placa = self.lstVeiculos.GetItemText(indice)
            try:                
                #deleta o veículo do banco
                VeiculoDAO.deleteVeiculo(placa)
                #para atualizar a Listctrl retirando o veículo que existia nela
                self.updateListctrl()                
            except:
                #caso o veículo não seja removido, uma caixa de diálogo será mostrada
                caixaDeDialogo = wx.MessageDialog(self,'Veículo inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Selecione um veículo.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
