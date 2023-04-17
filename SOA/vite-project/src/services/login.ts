import { postRequest, getRequest } from "./default";

type PostLoginResponse = {
    token: string;
};

export const login = async (
    email: string,
    senha: string
    ): Promise<PostLoginResponse> => {
    const response = await postRequest(`/conta/login`, {
        "email": email,
        "senha": senha,
        "tipo": "cliente"
    }).then((value) => {
        console.log('logado');
        return value
    }).catch(reason => {
        console.log(reason);
        return reason
    });

    console.log("oi",response)
    return response;
};