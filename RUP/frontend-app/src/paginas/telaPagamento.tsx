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
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="numeroCartao">Numero Cartao:</label>
                <input
                required
                type="text"
                name="numeroCartao"
                value={cartao.numeroCartao}
                onChange={handleInputChange}
                />
        
                <label htmlFor="cvvCartao">cvv:</label>
                <input
                required
                type="number"
                name="cvvCartao"
                value={cartao.cvvCartao}
                onChange={handleInputChange}
                />
        
                <label htmlFor="vencimento">Vencimento:</label>
                <input
                required
                type="date"
                name="vencimento"
                value={cartao.vencimento}
                onChange={handleInputChange}
                />

                <label htmlFor="nomeTitular">Nome Titular:</label>
                <input
                required
                type="text"
                name="nomeTitular"
                value={cartao.nomeTitular}
                onChange={handleInputChange}
                />

                <label htmlFor="cpfTitular">CPF do Titular:</label>
                <input
                required
                type="text"
                name="cpfTitular"
                value={cartao.cpfTitular}
                onChange={handleInputChange}
                />

                <label htmlFor="bandeira">Bandeira:</label>
                <input
                required
                type="text"
                name="bandeira"
                value={cartao.bandeira}
                onChange={handleInputChange}
                />
                <button type="submit">Pagar</button>
            </form>
            <h1>Pedido</h1>
            <ul>
                <li>clienteId: {pedido.clienteId}</li>
                <li>Valor total a pagar: {pedido.valor}</li>
                {pedido.itens.map(item => (
                    <li key={item.produto.id}>
                        nome: {item.produto.nome} - valor: R${item.produto.valor} - Estoque: {item.qtd}
                    </li>
                ))}
            </ul>
        </div>
      
      
    );
  };

