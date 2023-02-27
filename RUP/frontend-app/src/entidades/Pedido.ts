import { Item } from "./Item";

export interface Pedido {
    id:number;
    clienteId:number;
    valor:number;
    itens: Item[];
}

enum Statuspedido {
    FALHA=0,
    CONCLUIDO=1,
    ESPERANDO=2
}