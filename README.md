# Fantasy Football Parser for Mantra roles
Parser to get lists for **Por**, **Dif** (Dd, Dc, Ds), **Cen** (E, M, C), **Trq** (W, T) and **Att** (A, Pc) from a single list for the FantaAsta Live App, used for the Italian fantasy football in Mantra modality.

How to use:
- Download the .csv file from https://www.fantacalcio.it/app-fantaasta and place it into the same parser folder.
- Run in a terminal
  ```shell
  python3 parser.py filename
  ```

Example:
 - in the parser folder, using the example file 2024.csv, run
   ```shell
   python3 parser.py "2024.csv"
   ```

Next:
 - Lists for each role (Por, Dd, Ds, Dc, E, M, C, W, T, A, Pc).
 - Support with Euroleghe not tested.
 - Support automatic download with login.
