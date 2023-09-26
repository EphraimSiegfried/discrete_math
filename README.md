
# Discrete Mathematics in Computer Science Exercises

## Useful Links

- [Course website with slides](https://dmi.unibas.ch/en/studies/computer-science/courses-in-fall-semester-2023/lecture-discrete-mathematics-in-computer-science/)
- [ADAM course folder with exercises](https://adam.unibas.ch/goto_adam_crs_1547411.html)
- [Latex cheat sheet](/latex-cheat-sheet.pdf)

## Useful Commands

Copy paste the following commands in your terminal in the root project directory

**Generate new exercise folder with template in it:**

UNIX:

```bash
last_num=$(ls -d exercises/sheet*/ | grep -o '[0-9]*' | sort -n | tail -n 1); next_num=$(printf "%02d" $((last_num + 1))); new_folder="exercises/sheet$next_num"; mkdir -p "$new_folder"; cp template.tex "$new_folder/sheet$next_num.tex"

```

POWERSHELL:

```powershell
$lastNum = [int](Get-ChildItem -Path 'exercises' -Name -Directory | Sort-Object {[int]($_ -replace 'sheet', '')} | Select-Object -Last 1 -ExpandProperty Name -replace 'sheet', ''); $nextNum = '{0:D2}' -f ($lastNum + 1); $newFolder = "exercises\sheet$nextNum"; New-Item -Path $newFolder -ItemType Directory; Copy-Item 'template.tex' -Destination "$newFolder\sheet$nextNum.tex"

```
