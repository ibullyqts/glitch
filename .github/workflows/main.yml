name: DEVEL KA ABBU - 20 AGENT TOTAL BLACKOUT

on:
  workflow_dispatch:

jobs:
  blackout:
    runs-on: ubuntu-latest
    timeout-minutes: 360 
    strategy:
      fail-fast: false
      matrix:
        machine: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 10 Machines x 2 Agents = 20
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Selenium
        run: pip install selenium
      - name: Launch 20-Agent Matrix
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
          MACHINE_ID: ${{ matrix.machine }}
          PYTHONUNBUFFERED: "1"
        run: python -u praveer_gh.py
