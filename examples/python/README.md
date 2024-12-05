# System Info Script

This repository provides a script to retrieve system information using pre-generated protocol buffer definitions. Follow the steps below to set up and run the script.

---

## Prerequisites

Ensure you have the required Python package installed to generate the protocol buffers:

```bash
pip install grpcio-tools
```

---

## Generating Protocol Buffers

Run the following command to generate the necessary protocol buffer files:

```bash
./generate_protos
```

This will create the files required for the script to function correctly.

---

## Running the Script

Use the command below to execute the script.

**Note**:
- The `PYTHONPATH` is updated to include the directory containing the generated protocol buffer files, ensuring imports resolve correctly.
- The command assumes you are running it from the same directory as this `README.md`. If not modify the `PYTHONPATH` as needed.

```bash
PYTHONPATH=$PWD/generated_protos:$PYTHONPATH python3 get_system_info.py
```
