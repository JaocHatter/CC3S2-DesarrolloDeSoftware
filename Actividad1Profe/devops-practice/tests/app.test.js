const request = require('supertest');
const app = require('../src/app');

describe('GET /', () => {
    let server;

    beforeAll(() => {
        server = app.listen(0); // Usar 0 permite al sistema asignar un puerto libre
    });

    afterAll(() => {
        server.close(); // Cierra el servidor después de que las pruebas hayan terminado
    });

    it('should return Hello, World!', async () => {
        const res = await request(server).get('/');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('Hello, World!');
    });
});
