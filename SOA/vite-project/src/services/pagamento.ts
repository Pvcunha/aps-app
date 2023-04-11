import { Pedido } from "../entidades/Pedido";
import { postRequest } from "./default";

export const pagarPedido = async (
    pedido: Pedido,
    dadosDoPagamento: any
): Promise<void> => {
    const response = await postRequest('/finalizarPedido',{
        pedido,
        dadosDoPagamento
    });
    return response;
};
