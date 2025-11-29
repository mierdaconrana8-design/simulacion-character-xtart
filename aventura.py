#!/usr/bin/env python3
import sys

class Game:
    def __init__(self):
        self.location = "playa"
        self.inventory = {"espada": 1, "alforjas": 1}
        self.flags = {
            "cuerda": False,
            "caracola": False,
            "carta": False,
            "llave": False,
            "mapa": False,
            "bebio_verde": False,
            "caracola_entregada": False
        }
        self.playing = True

    def run(self):
        print("Te despiertas en la playa. Tu aventura comienza...")
        while self.playing:
            getattr(self, self.location)()

    def input(self, msg, options):
        print(msg)
        for o in options:
            print(" -", o)
        while True:
            x = input("> ").lower().strip()
            if x in options:
                return x
            print("Opción no válida.")

    def playa(self):
        print("\nPLAYA — Solo llevas tu espada y alforjas.")
        choice = self.input("Opciones:", [
            "ir al este",
            "ir al oeste",
            "ir al sur"
        ])
        if choice == "ir al este": self.location = "campamento"
        if choice == "ir al oeste": self.location = "acantilado"
        if choice == "ir al sur": self.location = "jungla"

    def campamento(self):
        print("\nCAMPAMENTO — Hay comida podrida, una carta y una cuerda.")
        choice = self.input("Opciones:", [
            "ir al este",
            "recoger cuerda",
            "leer carta"
        ])
        if choice == "ir al este": self.location = "playa"
        if choice == "recoger cuerda":
            self.flags["cuerda"] = True
            print("Has recogido la cuerda.")
        if choice == "leer carta":
            print("\nLa carta dice que el gato del capitán se llama AMARO.")
            self.flags["carta"] = True

    def acantilado(self):
        print("\nACANTILADO — 20 metros de caída, abajo hay una abertura.")
        options = ["ir al oeste", "bajar sin cuerda"]
        if self.flags["cuerda"]:
            options.append("bajar con cuerda")
        choice = self.input("Opciones:", options)

        if choice == "ir al oeste":
            self.location = "playa"
        elif choice == "bajar sin cuerda":
            print("Caes al vacío. GAME OVER.")
            self.playing = False
        elif choice == "bajar con cuerda":
            print("Desciendes con la cuerda hasta la abertura.")
            self.location = "abertura"

    def abertura(self):
        print("\nABERTURA — Hay restos de barcos y una caracola nacarada.")
        choice = self.input("Opciones:", [
            "subir acantilado",
            "coger caracola"
        ])
        if choice == "subir acantilado":
            self.location = "acantilado"
        else:
            self.flags["caracola"] = True
            print("Guardas la caracola.")

    def jungla(self):
        print("\nJUNGLA — Llegas hambriento a un estanque con ranas.")
        choice = self.input("Opciones:", [
            "buscar frutas",
            "cazar ranas",
            "ir al norte",
            "ir al sur"
        ])
        if choice == "buscar frutas":
            print("Encuentras frutas y recuperas fuerzas.")
        elif choice == "cazar ranas":
            print("Las ranas están venenosas. GAME OVER.")
            self.playing = False
            return
        elif choice == "ir al norte": self.location = "playa"
        elif choice == "ir al sur": self.location = "templo_exterior"

    def templo_exterior(self):
        print("\nTEMPLO EXTERIOR — Un ser extraño te pide algo del mar.")
        options = ["luchar", "huir", "dialogar"]
        choice = self.input("Opciones:", options)

        if choice == "luchar":
            print("La criatura te destruye fácilmente. GAME OVER.")
            self.playing = False
        elif choice == "huir":
            self.location = "jungla"
        else:
            if self.flags["caracola"]:
                print("Le entregas la caracola. Te deja pasar al interior.")
                self.flags["caracola_entregada"] = True
                self.location = "templo_interior"
            else:
                print("No tienes nada del mar. Huyes.")
                self.location = "jungla"

    def templo_interior(self):
        print("\nTEMPLO INTERIOR — Hay 6 botellas de colores.")
        print("Solo una es correcta...")

        choice = self.input("Elige botella:", [
            "amarilla",
            "roja",
            "verde",
            "azul",
            "morada",
            "negra"
        ])

        if choice == "verde":
            print("Puedes meter la mano en las brasas y abres un paso a una cueva.")
            self.flags["bebio_verde"] = True
            self.location = "cueva"
        elif choice in ["amarilla", "azul", "morada"]:
            print("Era veneno. GAME OVER.")
            self.playing = False
        else:
            print("No pasa nada.")
            self.location = "templo_interior"

    def cueva(self):
        print("\nCUEVA — Ves “La Venganza de la Reina Ana”.")
        options = ["observar agua", "entrar barco"]
        if self.flags["mapa"]:
            options.append("nadar túnel")
        choice = self.input("Opciones:", options)

        if choice == "observar agua":
            print("La salida al mar está colapsada.")
        elif choice == "entrar barco":
            self.location = "barco"
        elif choice == "nadar túnel":
            self.location = "playa_sur"

    def barco(self):
        print("\nBARCO — Un gato esquelético con una llave te observa.")
        choice = self.input("Opciones:", [
            "volver a la cueva",
            "quitar llave",
            "llamar por nombre"
        ])
        if choice == "volver a la cueva":
            self.location = "cueva"
        elif choice == "quitar llave":
            print("Le quitas la llave.")
            self.flags["llave"] = True
            self.location = "barco"
        else:
            name = input("Nombre del gato > ").strip().lower()
            if name == "amaro":
                print("El gato abre la bodega para ti.")
                self.flags["llave"] = True
                self.location = "bodega"
            else:
                print("El gato no reacciona.")

    def bodega(self):
        print("\nBODEGA — Encuentras un mapa secreto.")
        self.flags["mapa"] = True
        choice = self.input("Opciones:", [
            "llenar bolsillos",
            "salir barco"
        ])
        if choice == "llenar bolsillos":
            print("Guardas tesoro en tus alforjas.")
        self.location = "barco"

    def playa_sur(self):
        print("\nPLAYA SUR — Tu tripulación repara el barco.")
        print("Has sobrevivido. FIN.")
        self.playing = False

if __name__ == "__main__":
    Game().run()
