name: DEVEL KA ABBU - 10 AGENT OMNIPRESENCE

on:
  workflow_dispatch:

jobs:
  blitz:
    runs-on: ubuntu-latest
    timeout-minutes: 360 # 6-hour maximum pressure
    strategy:
      fail-fast: false
      matrix:
        machine: [1, 2, 3, 4, 5] # Launches 5 runners in parallel
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Selenium
        run: pip install selenium
      - name: Launch 10-Agent Blitz
        env:
          SESSION_ID: ${{ secrets.SESSION_ID }}
          GROUP_URL: ${{ secrets.GROUP_URL }}
          TARGET_NAME: ${{ secrets.TARGET_NAME }}
          MACHINE_ID: ${{ matrix.machine }}
          PYTHONUNBUFFERED: "1"
        run: python -u praveer_gh.py
