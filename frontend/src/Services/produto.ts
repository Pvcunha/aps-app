import { Produto } from "../entidades/Produto";
import { getRequest } from "./default";


type PegaProdutoResponse ={
    produto:Produto;
}

export const PegarProduto = async (id: number): Promise<PegaProdutoResponse> => {
    const response = await getRequest(`/produto/${id}`);
    return response;
};