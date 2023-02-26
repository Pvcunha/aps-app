import { Item } from "../entidades/Item";
import { getRequest } from "./default";

type GetEstoqueResponse = Item[]

export const getEstoque =  async(
    filtro?: string 
): Promise<GetEstoqueResponse> => {
    const response = await getRequest('/estoque',undefined, {
        nome:filtro
    });
    return response
}