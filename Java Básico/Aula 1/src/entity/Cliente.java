package entity;

public class Cliente {

    private String name;
    private String number;

    public void nomeCliente(){
        System.out.println("Olá, " + this.name + ". seu número é " + this.number);
    }

    public static void main(String[] args) {

        System.out.println("Hello, world!");

        Cliente cliente1 = new Cliente();

        cliente1.name = "taylor swift";
        cliente1.number = "13";

        cliente1.nomeCliente();

        //numeros
        Integer num = 123;
        Double pi = 3.14;
    }
}
