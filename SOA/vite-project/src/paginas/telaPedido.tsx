import React, { FormEvent, useState } from "react";
import { Pedido } from "../entidades/Pedido";

export const TelaPedido: React.FC = () => {
  const [pedido, setPedido] = useState<Pedido>({
    id: -1,
    clienteId: 0,
    valor: 3.5,
    itens: [{ produto: { id: 0, nome: "Coxinha", valor: 3.5 }, qtd: 1 }],
  });

  const handleIrAoPagamento = () => {
    // Redireciona para a tela de pagamento com os dados do pedido
    window.location.href = `/pagamento?pedido=${JSON.stringify(pedido)}`;
  };

  return (
    <div style={{ backgroundColor: "beige", height: "100vh", width: "100vw" }}>
      <h1 style={{ textAlign: "center" }}>Pedido</h1>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <ul style={{ textAlign: "left" }}>
          <li>clienteId: {pedido.clienteId}</li>
          <li>Valor total a pagar: {pedido.valor}</li>
          {pedido.itens.map((item) => (
            <li key={item.produto.id}>
              nome: {item.produto.nome} - valor: R${item.produto.valor} - Estoque: {item.qtd}
            </li>
          ))}
        </ul>
      </div>
      <div style={{ display: "flex", justifyContent: "center", marginTop: "20px" }}>
        <button onClick={handleIrAoPagamento}>Ir ao pagamento</button>
      </div>
    </div>
  );
};
