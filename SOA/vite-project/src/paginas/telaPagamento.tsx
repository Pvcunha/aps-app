import React, { FormEvent, useEffect, useState } from "react";
import { pagarPedido } from "../services/pagamento";
import { Pedido } from "../entidades/Pedido";
import axios from "axios";


interface PagamentoFormProps {
  numeroCartao: string;
  cvvCartao: string;
  vencimento: string;
  nomeTitular: string;
  cpfTitular: string;
  bandeira: string;
  valorPagamento: number;
}

export const TelaPagamento: React.FC = () => {
  /*const [pedido, setPedido] = useState<Pedido | null>(null);

  useEffect(() => {
    // Get the order data from the URL query string
    const searchParams = new URLSearchParams(window.location.search);
    const pedidoStr = searchParams.get("pedido");
    setPedido(JSON.parse(pedidoStr));
  }, []);
*/
  const tok = localStorage.getItem("confirmação");
  const decodedTo = JSON.parse(tok);
  const { pedidoID,precoTotal } = decodedTo;

  const [cartao, setCartao] = useState<PagamentoFormProps>({
    numeroCartao: "",
    cvvCartao: "",
    vencimento: "",
    nomeTitular: "",
    cpfTitular: "",
    bandeira: "mockapi",
    valorPagamento: 0,
  });

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const requestBody = {
      "pedido": {
        "id": pedidoID,
        "precoTotal": precoTotal,
      },
      "dadosDoPagamento": {
        "bandeira": cartao.bandeira,
        "numeroCartao": cartao.numeroCartao,
        "cpf": cartao.cpfTitular,
        "nomeTitular": cartao.nomeTitular,
        "cvv": cartao.cvvCartao,
        "vencimento": cartao.vencimento,
      },
    };
    console.log(requestBody)
    const response = await axios.post("http://localhost:3030/pagamento/pagamento",requestBody);
    console.log(response.data);
    
  };

  const handleInputChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = event.target;
    setCartao((prevCartao) => ({
      ...prevCartao,
      [name]: value,
    }));
  };
  
    return (
        <div style={{backgroundColor:"beige",height: "100vh", width: "100vw"}}>
            <h1 style={{textAlign: "center"}}>Pagamento</h1>
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
                </div>
                <button type="submit" style={{display:"block", margin: "auto", marginTop:"15px"}}>Finalizar Pagamento</button>
            </form>
        </div>
    );
    
  };

