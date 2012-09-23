# -*- coding: latin-1 -*-
#Boa:Frame:frmDevolucao

import wx
import wx.lib.stattext
import wx.lib.masked.textctrl
import wx.lib.buttons

from db.ClienteDAO import *
from db.VeiculoDAO import *
from db.TipoVeiculoDAO import TipoVeiculoDAO
from datetime import *
from negocio.Locacao import *
from db.LocacaoDAO import *
from negocio.Historico import *
from db.HistoricoDAO import *


def create(parent):
    return frmDevolucao(parent)

[wxID_FRMDEVOLUCAO, wxID_FRMDEVOLUCAOBTNCALCULAR, 
 wxID_FRMDEVOLUCAO, wxID_FRMDEVOLUCAOBTNCALCULARSEMCAUCAO,
 wxID_FRMDEVOLUCAOBTNCANCELAR, wxID_FRMDEVOLUCAOBTNCPF,
 wxID_FRMDEVOLUCAOBTNFINALIZAR, wxID_FRMDEVOLUCAOBTNPLACA, 
 wxID_FRMDEVOLUCAOLBLCPF, wxID_FRMDEVOLUCAOLBLPLACA, 
 wxID_FRMDEVOLUCAOLSTBUSCA, wxID_FRMDEVOLUCAOPNLDEVOLUCAO, 
 wxID_FRMDEVOLUCAOSTBUSCAR, wxID_FRMDEVOLUCAOSTCALCULAR, 
 wxID_FRMDEVOLUCAOSTKMCHEGADA, wxID_FRMDEVOLUCAOSTRESULTADO, 
 wxID_FRMDEVOLUCAOSTTOTAL, wxID_FRMDEVOLUCAOSTVALOR, wxID_FRMDEVOLUCAOTXTCPF, 
 wxID_FRMDEVOLUCAOTXTKMCHEGADA, wxID_FRMDEVOLUCAOTXTPLACA, wxID_FRMDEVOLUCAOLISTCTRLBUSCALOCACAO, 
 wxID_FRMDEVOLUCAOSTNOMECLIENTE
] = [wx.NewId() for _init_ctrls in range(23)]

class frmDevolucao(wx.Frame):
    def _init_coll_listCtrlBuscaLocacao_Columns(self,parent):
        # generated method, don't edit
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Id',
              width=45)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Data',
              width=155)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='CPF',
              width=95)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Placa',
              width=70)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Modelo',
              width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Km Saída',
              width=70)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Valor Parcial',
              width=90)
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMDEVOLUCAO, name=u'frmDevolucao',
              parent=prnt, pos=wx.Point(454, 116), size=wx.Size(786, 459),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION,
              title=u'Devolu\xe7\xe3o')
        self.SetClientSize(wx.Size(770, 424))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',
              wx.BITMAP_TYPE_ICO))

        self.pnlDevolucao = wx.Panel(id=wxID_FRMDEVOLUCAOPNLDEVOLUCAO,
              name=u'pnlDevolucao', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(770, 424), style=wx.TAB_TRAVERSAL)

        self.stBuscar = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTBUSCAR,
              label=u'Buscar Loca\xe7\xe3o', name=u'stBuscar',
              parent=self.pnlDevolucao, pos=wx.Point(128, 8), size=wx.Size(632,
              96), style=0)

        self.btnFinalizar = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNFINALIZAR,
              label=u'Finalizar', name=u'btnFinalizar',
              parent=self.pnlDevolucao, pos=wx.Point(24, 24), size=wx.Size(76,
              25), style=0)
        self.btnFinalizar.Bind(wx.EVT_BUTTON, self.OnBtnFinalizarButton,
              id=wxID_FRMDEVOLUCAOBTNFINALIZAR)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlDevolucao,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMDEVOLUCAOBTNCANCELAR)

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMDEVOLUCAOTXTCPF,
              name=u'txtCpf', parent=self.pnlDevolucao, pos=wx.Point(144, 56),
              size=wx.Size(160, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)

        self.lblCpf = wx.lib.stattext.GenStaticText(ID=wxID_FRMDEVOLUCAOLBLCPF,
              label=u'CPF :', name=u'lblCpf', parent=self.pnlDevolucao,
              pos=wx.Point(144, 40), size=wx.Size(27, 13), style=0)

        self.lblPlaca = wx.lib.stattext.GenStaticText(ID=wxID_FRMDEVOLUCAOLBLPLACA,
              label=u'Placa :', name=u'lblPlaca', parent=self.pnlDevolucao,
              pos=wx.Point(376, 40), size=wx.Size(33, 13), style=0)

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMDEVOLUCAOTXTPLACA,
              name=u'txtPlaca', parent=self.pnlDevolucao, pos=wx.Point(376, 56),
              size=wx.Size(152, 21), style=0, value=u'   -    ')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')

        self.lstBusca = wx.ListCtrl(id=wxID_FRMDEVOLUCAOLSTBUSCA,
              name=u'lstBusca', parent=self.pnlDevolucao, pos=wx.Point(144,
              136), style=wx.LC_ICON)

        self.stKmChegada = wx.StaticText(id=wxID_FRMDEVOLUCAOSTKMCHEGADA,
              label=u'KM Chegada :', name=u'stKmChegada',
              parent=self.pnlDevolucao, pos=wx.Point(144, 352), size=wx.Size(68,
              16), style=0)

        self.txtKmChegada = wx.TextCtrl(id=wxID_FRMDEVOLUCAOTXTKMCHEGADA,
              name=u'txtKmChegada', parent=self.pnlDevolucao, pos=wx.Point(144,
              368), size=wx.Size(160, 21), style=0, value=u'')

        self.btnCalcular = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNCALCULAR,
              label=u'Com caução', name=u'btnCalcular', parent=self.pnlDevolucao,
              pos=wx.Point(315, 338), size=wx.Size(80, 28), style=0)
        self.btnCalcular.Bind(wx.EVT_BUTTON, self.OnBtnCalcularButtonComCaucao,
              id=wxID_FRMDEVOLUCAOBTNCALCULAR)
        
        self.btnCalcularSemCaucao = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNCALCULARSEMCAUCAO,
              label=u'Sem caução', name=u'btnCalcularSemCaucao', parent=self.pnlDevolucao,
              pos=wx.Point(315, 378), size=wx.Size(80, 28), style=0)
        self.btnCalcularSemCaucao.Bind(wx.EVT_BUTTON, self.OnBtnCalcularButtonSemCaucao,
              id=wxID_FRMDEVOLUCAOBTNCALCULARSEMCAUCAO)

        self.stValor = wx.StaticText(id=wxID_FRMDEVOLUCAOSTVALOR,
              label=u'Valor a Pagar :', name=u'stValor',
              parent=self.pnlDevolucao, pos=wx.Point(464, 352), size=wx.Size(72,
              13), style=0)

        self.stTotal = wx.StaticText(id=wxID_FRMDEVOLUCAOSTTOTAL,
              label=u'R$ 00,00', name=u'stTotal', parent=self.pnlDevolucao,
              pos=wx.Point(464, 368), size=wx.Size(82, 19), style=0)
        self.stTotal.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.btnCpf = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMDEVOLUCAOBTNCPF, name=u'btnCpf',
              parent=self.pnlDevolucao, pos=wx.Point(312, 48), size=wx.Size(32,
              32), style=0)
        self.btnCpf.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarCpfButton,
              id=wxID_FRMDEVOLUCAOBTNCPF)

        self.btnPlaca = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMDEVOLUCAOBTNPLACA,
              name=u'btnPlaca', parent=self.pnlDevolucao, pos=wx.Point(536, 48),
              size=wx.Size(32, 32), style=0)
        self.btnPlaca.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarPlacaButton,
              id=wxID_FRMDEVOLUCAOBTNPLACA)


        self.stResultado = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTRESULTADO,
              label=u'Resultado da busca', name=u'stResultado',
              parent=self.pnlDevolucao, pos=wx.Point(128, 112),
              size=wx.Size(632, 200), style=0)
        
        self.listCtrlBuscaLocacao = wx.ListCtrl(id=wxID_FRMDEVOLUCAOLISTCTRLBUSCALOCACAO,
              name='listCtrlBuscaLocacao', parent=self.pnlDevolucao, pos=wx.Point(144,
              136), size=wx.Size(600, 160), style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaLocacao_Columns(self.listCtrlBuscaLocacao)

        self.stCalcular = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTCALCULAR,
              label=u'Calcular Pagamento', name=u'stCalcular',
              parent=self.pnlDevolucao, pos=wx.Point(128, 320),
              size=wx.Size(632, 96), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.calculoFeito = False
        #self.inserirDadosNasColunasDaTabelaLocacao(self.listCtrlBuscaLocacao)
        
    def criarTabela(self):
        self.listCtrlBuscaLocacao = wx.ListCtrl(id=wxID_FRMDEVOLUCAOLISTCTRLBUSCALOCACAO,
              name='listCtrlBuscaLocacao', parent=self.pnlDevolucao,
              pos=wx.Point(144,136), size=wx.Size(600, 170), style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaLocacao_Columns(self.listCtrlBuscaLocacao)
        
    def OnBtnPesquisarCpfButton(self, event):
        self.listCtrlBuscaLocacao.Destroy()  
        self.calculoFeito = False
        cpf = self.txtCpf.GetValue() 
        #print cpf
        
        self.criarTabela()
        #print ClienteDAO.verificarExistenciaCliente(cpf)
        if(ClienteDAO.verificarExistenciaCliente(cpf) is True):
            #insere na tabela os dados de acordo com a cor fornecida
            self.inserirInformacoesNaListctrlByCpf(self.listCtrlBuscaLocacao, cpf)
            
            self.txtCpf.Clear()
                    
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtCpf.Clear()
            
            
    def inserirInformacoesNaListctrlByCpf(self,listCtrl,cpf):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega as locacoes feitas pelo respectivo CPF
        rows = LocacaoDAO.getLocacoesByCpf(cpf)        
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
        
    def OnBtnPesquisarPlacaButton(self, event):
        self.listCtrlBuscaLocacao.Destroy()  
        self.calculoFeito = False
        placa = self.txtPlaca.GetValue().upper() 
        #print placa
        
        self.criarTabela()
        #print VeiculoDAO.verificarExistenciaVeiculo(placa)
        if(VeiculoDAO.verificarExistenciaVeiculo(placa) is True):
            #insere na tabela os dados de acordo com a cor fornecida
            self.inserirInformacoesNaListctrlByPlaca(self.listCtrlBuscaLocacao, placa)
            
            self.txtPlaca.Clear()
                    
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Veículo inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtPlaca.Clear()
    
    def inserirInformacoesNaListctrlByPlaca(self,listCtrl,placa):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega as locacoes feitas pela respectiva placa
        rows = LocacaoDAO.getLocacoesByPlaca(placa)        
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
        
    
    def inserirDadosNasColunasDaTabelaDeResultados(self,listCtrl,rows):        
        #Método responsável por colocar as informações do banco nas colunas da ListCtrl.
        #Desenvolvido para evitar a repetição de código nos 3 tipos de buscas de um veículo.
        #Recebe como parâmetro a ListCtrl na qual deseja inserir dados e as linhas
        #de informações obtidas numa busca no banco de dados.
        if rows:
            for row in rows:
                num_itens = listCtrl.GetItemCount()
                listCtrl.InsertStringItem(num_itens,str(row[0]))
                listCtrl.SetStringItem(num_itens,1,row[1])
                listCtrl.SetStringItem(num_itens,2,row[4])
                listCtrl.SetStringItem(num_itens,3,row[5])
                listCtrl.SetStringItem(num_itens,5,str(row[3]))
                listCtrl.SetStringItem(num_itens,6,str(row[2]))
                
                veiculos = VeiculoDAO.getAllVeiculos()
                for i in veiculos:
                    if i[1] == row[5]:
                        modelo = i[4]
                #referente à tabela de tipo de veículos
                listCtrl.SetStringItem(num_itens,4,str(modelo))

    def OnBtnCancelarButton(self, event):
        self.listCtrlBuscaLocacao.Destroy()
        self.criarTabela()
        self.txtKmChegada.Clear()
        self.stTotal.SetLabel("R$ 00,00")
        
    def getObjetosLocacao(self, idLocacao):
        #Encontrar dados de locacao a partir do idLocacao
        locacao = LocacaoDAO().procurarLocacaoById(idLocacao)
    
        #Encontrar o id do tipoVeiculo e do Veiculo pela placa              
        veiculos = VeiculoDAO().getAllVeiculos()
        placa = locacao.getPlacaVeiculo()
        for i in veiculos:
            if (i[1] == placa):
                idTipo = i[6]
                idVeiculo = i[0]
                    
        tipoVeiculo = TipoVeiculoDAO.procurarTipo(idTipo)
        veiculo = VeiculoDAO.procurarVeiculoById(idVeiculo)
            
        listaObjetos = [locacao, tipoVeiculo, veiculo]
        return listaObjetos
    

    def OnBtnCalcularButtonComCaucao(self, event):
        #pegar o indice do item selecionado no Listctrl
        indice = self.listCtrlBuscaLocacao.GetFocusedItem()
        #print indice
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            idLocacao = self.listCtrlBuscaLocacao.GetItemText(indice)
            print idLocacao
                        
            #buscar todos os objetos relacionados à locacao        
            listaObjetos = self.getObjetosLocacao(idLocacao)
            
            tipoVeiculo = listaObjetos[1]
            locacao = listaObjetos[0]
        
            valorContaParcial = locacao.getValorContaParcial()
            #print valorContaParcial
            precoKm = tipoVeiculo.getPrecoKm()
            #print precoKm
            
            quilometragemDeChegada = self.txtKmChegada.GetValue()
            #print int(quilometragemDeChegada)
            if quilometragemDeChegada != "":
                kmRodados = int(quilometragemDeChegada) - locacao.getQuilometragemDeSaida()
                if kmRodados > 0:
                    valorContaTotal =  valorContaParcial + (precoKm * kmRodados)
                    #print valorContaTotal
                
                    self.stTotal.SetLabel("R$ %.2f" %(valorContaTotal))
                
                    caixaDeMensagem = wx.MessageDialog(self,'Valor de locação calculado!', 'CONFIRMAÇÃO', wx.OK | wx.ICON_INFORMATION)
                    caixaDeMensagem.ShowModal()
                    caixaDeMensagem.Destroy()
                
                    self.calculoFeito = True
                else:
                    caixaDeMensagem = wx.MessageDialog(self,'Valor de quilometragem menor que a última cadastrada!', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                    caixaDeMensagem.ShowModal()
                    caixaDeMensagem.Destroy()
            else:
                caixaDeMensagem = wx.MessageDialog(self,'Informe a quilometragem de chegada!', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeMensagem.ShowModal()
                caixaDeMensagem.Destroy()
                
        else:            
                caixaDeMensagem = wx.MessageDialog(self,'Selecione a locação.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeMensagem.ShowModal()
                caixaDeMensagem.Destroy()
                
    def OnBtnCalcularButtonSemCaucao(self, event):
        #pegar o indice do item selecionado no Listctrl
        indice = self.listCtrlBuscaLocacao.GetFocusedItem()
        #print indice
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            idLocacao = self.listCtrlBuscaLocacao.GetItemText(indice)
            print idLocacao
                        
            #buscar todos os objetos relacionados à locacao        
            listaObjetos = self.getObjetosLocacao(idLocacao)
            
            tipoVeiculo = listaObjetos[1]
            locacao = listaObjetos[0]
        
            valorContaParcial = locacao.getValorContaParcial()
            #print valorContaParcial
            precoKm = tipoVeiculo.getPrecoKm()
            #print precoKm
            
            quilometragemDeChegada = self.txtKmChegada.GetValue()
            #print int(quilometragemDeChegada)
            if quilometragemDeChegada != "":
                kmRodados = int(quilometragemDeChegada) - locacao.getQuilometragemDeSaida()
                if kmRodados > 0:
                    valorContaTotal =  tipoVeiculo.getTaxaBase() + (precoKm * kmRodados)
                    #print valorContaTotal
                
                    self.stTotal.SetLabel("R$ %.2f" %(valorContaTotal))
                
                    caixaDeMensagem = wx.MessageDialog(self,'Valor de locação calculado!', 'CONFIRMAÇÃO', wx.OK | wx.ICON_INFORMATION)
                    caixaDeMensagem.ShowModal()
                    caixaDeMensagem.Destroy()
                
                    self.calculoFeito = True
                else:
                    caixaDeMensagem = wx.MessageDialog(self,'Valor de quilometragem menor que a última cadastrada!', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                    caixaDeMensagem.ShowModal()
                    caixaDeMensagem.Destroy()
            else:
                caixaDeMensagem = wx.MessageDialog(self,'Informe a quilometragem de chegada!', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeMensagem.ShowModal()
                caixaDeMensagem.Destroy()
                
        else:            
                caixaDeMensagem = wx.MessageDialog(self,'Selecione a locação.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeMensagem.ShowModal()
                caixaDeMensagem.Destroy()
                
    def OnBtnFinalizarButton(self, event):
        if (self.calculoFeito == True):
            indice = self.listCtrlBuscaLocacao.GetFocusedItem()
            if indice != -1: 
                idLocacao = self.listCtrlBuscaLocacao.GetItemText(indice)
                listaObjetos = self.getObjetosLocacao(idLocacao)
                if listaObjetos != []:
                    veiculo = listaObjetos[2]
                    
                    #Encontrar veiculo pelo id
                    idVeiculo = veiculo.getIdVeiculo()
                    veiculoLocado = VeiculoDAO().procurarVeiculoById(idVeiculo)
                    
                    #Atualizar a quilometragem do veiculo
                    quilometragemAtual = int(self.txtKmChegada.GetValue())
                    
                    #Alterar dados do veiculo
                    veiculoLocado.setQuilometragemAtual(quilometragemAtual)
                    veiculoLocado.setDisponibilidade("DISPONIVEL")
                    
                    #Manter alteracoes no banco de dados
                    VeiculoDAO().updateVeiculo(veiculoLocado)
                    
                    #Cadastrar no banco Historico
                    locacao = listaObjetos[0]
                    
                    #Criar objeto historico
                    dataLocacao = locacao.getDataLocacao()
                    dataDevolucao = datetime.now()
                    quilometragemDeSaida = locacao.getQuilometragemDeSaida()
                    quilometragemDeChegada = quilometragemAtual
                    cpfCliente = locacao.getCpfCliente()
                    placaCarro = locacao.getPlacaVeiculo()
                    valorContaTotal = (self.stTotal.GetLabel())[3:]
                    
                    historico = Historico(dataLocacao, dataDevolucao, quilometragemDeSaida, quilometragemDeChegada, placaCarro, cpfCliente, valorContaTotal)
                    #Adicionar no banco
                    HistoricoDAO.insertHistorico(historico)
                    LocacaoDAO.deleteLocacao(idLocacao)
                    self.listCtrlBuscaLocacao.Destroy()
                    self.criarTabela()
                    caixaDeMensagem = wx.MessageDialog(self,'Devolução concluída!', 'CONFIRMAÇÃO', wx.OK | wx.ICON_INFORMATION)
                    caixaDeMensagem.ShowModal()
                    caixaDeMensagem.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
