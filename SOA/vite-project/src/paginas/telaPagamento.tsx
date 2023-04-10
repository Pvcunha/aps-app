import React, { FormEvent, useState } from "react";
import { pagarPedido } from "../services/pagamento";
import { Pedido } from "../entidades/Pedido";

interface PagamentoFormProps  {
    numeroCartao: string;
    cvvCartao: string;
    vencimento: string;
    nomeTitular: string;
    cpfTitular: string;
    bandeira: string;
    valorPagamento: number;
}

export const TelaPagamento: React.FC = () => {
    const [pedido, setPedido] = useState<Pedido>({
        id: -1,
        clienteId: 0,
        valor: 3.5,
        itens: [ {produto: { id: 0, nome: "Coxinha", valor: 3.5 }, qtd:1}]
    })

    const [cartao, setCartao] = useState<PagamentoFormProps>({
        numeroCartao: "",
        cvvCartao: "",
        vencimento: "",
        nomeTitular: "",
        cpfTitular: "",
        bandeira: "mockapi",
        valorPagamento: 0
    });
  
    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      pagarPedido(pedido, cartao);
    };
  
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      const {name, value } = event.target;
      setCartao((prevcartao) => ({
        ...prevcartao,
        [name]: value,
      }));
    };
  
    return (
        <div style={{backgroundColor:"beige",height: "100vh", width: "100vw"}}>
            <h1 style={{textAlign: "center"}}>Pedido</h1>
            <div style={{display: "flex", justifyContent: "center"}}>
                <ul style={{textAlign: "left"}}>
                <li>clienteId: {pedido.clienteId}</li>
                <li>Valor total a pagar: {pedido.valor}</li>
                {pedido.itens.map(item => (
                    <li key={item.produto.id}>
                    nome: {item.produto.nome} - valor: R${item.produto.valor} - Estoque: {item.qtd}
                    </li>
                ))}
                </ul>
            </div>
            <form onSubmit={handleSubmit}>
                <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
                    <label htmlFor="numeroCartao" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px" }}>Numero Cartao:</label>
                    <input
                        required
                        type="text"
                        name="numeroCartao"
                        value={cartao.numeroCartao}
                        onChange={handleInputChange}
                    />

                    <label htmlFor="cvvCartao" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px"}}>cvv:</label>
                    <input
                        required
                        type="number"
                        name="cvvCartao"
                        value={cartao.cvvCartao}
                        onChange={handleInputChange}
                    />

                    <label htmlFor="vencimento" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px"}}>Vencimento:</label>
                    <input
                        required
                        type="date"
                        name="vencimento"
                        value={cartao.vencimento}
                        onChange={handleInputChange}
                    />

                    <label htmlFor="nomeTitular" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px"}}>Nome Titular:</label>
                    <input
                        required
                        type="text"
                        name="nomeTitular"
                        value={cartao.nomeTitular}
                        onChange={handleInputChange}
                    />

                    <label htmlFor="cpfTitular" style={{textAlign: "left",marginTop: "15px",marginBottom:"15px"}}>CPF do Titular:</label>
                    <input
                        required
                        type="text"
                        name="cpfTitular"
                        value={cartao.cpfTitular}
                        onChange={handleInputChange}
                    />

                    <label htmlFor="bandeira" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px"}}>Bandeira:</label>
                    <input
                        required
                        type="text"
                        name="bandeira"
                        value={cartao.bandeira}
                        onChange={handleInputChange}
                    />
                <button type="submit" style={{textAlign: "center",marginTop: "15px",marginBottom:"15px"}}>Pagar</button>
                </div>
                
            </form>
    </div>

      
      
    );
  };

