import sys

class GateSolver:
    def __init__(self, filename):
        self.filename = filename
        self.operations = {
            "AND": lambda x, y: self.get_wire(x) & self.get_wire(y),
            "OR": lambda x, y: self.get_wire(x) | self.get_wire(y),
            "NOT": lambda x: 0xFFFF & ~(self.get_wire(x)),
            "RSHIFT": lambda x, y: self.get_wire(x) >> self.get_wire(y),
            "LSHIFT": lambda x, y: self.get_wire(x) << self.get_wire(y),
        }
        self.wire_outputs = {}
        self.gates = {}

    def get_gates_from_file(self):
        self.gates = {}
        try:
            with open(self.filename, "r") as input_file:
                for line in input_file.readlines():
                    line = line.strip()
                    if (line == ""):
                        continue
                    (operands, wire) = line.split(" -> ")
                    self.gates[wire] = operands.split(" ")
        except FileNotFoundError:
            print("File " + filename + " not found")
        return self.gates

    def get_wire(self, wire):
        if len(self.gates.keys()) == 0:
            self.gates = self.get_gates_from_file()
            if len(self.gates.keys()) == 0:
                return None

        if (wire.isnumeric()):
            return int(wire)

        if wire not in self.wire_outputs:
            operands = self.gates[wire]
            if len(operands) == 1:
                output = self.get_wire(operands[0])
            else:
                gate = operands.pop(-2)
                output = self.operations[gate](*operands)
            self.wire_outputs[wire] = output
        return self.wire_outputs[wire]

def main():
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
        filename = "input_file.txt"
    solver = GateSolver(filename)
    print("Wire a:", solver.get_wire("a"))

if __name__ == "__main__":
    main()
