import { Pedido } from "../entidades/Pedido";
import { getRequest,postRequest } from "./default";

export const PegarPedido = async (id:number): Promise<Pedido> => {
    const token = localStorage.getItem("token");
    const response = await getRequest(`/pedidos/${id}`, token?.toString());
    return response;
}
// N coloquei a de pegar todos os pedidos 

export const realizarPedido = async (
    metodoPagamento: string,
    dadosDoPagamento: any
  ): Promise<Pedido> => {
    const token = localStorage.getItem("token");
    const response = await postRequest(`/realizarpedido`,
      {
        metodoPagamento,
        dadosDoPagamento
      },
      token?.toString()
    );
    return response;
  };