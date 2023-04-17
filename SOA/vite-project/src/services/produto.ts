import { Produto } from "../entidades/Produto";
import { getRequest } from "./default";


type PegaProdutoResponse = {
    produto:Produto;
}

    export const PegarProduto = async (): Promise<PegaProdutoResponse> => {
        const response = await getRequest(`/estoque/listaItens`);
        return response.data;
    };