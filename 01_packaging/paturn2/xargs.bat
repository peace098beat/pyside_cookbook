@echo off
rem 引数が無いとき
if "%~1"=="" (
echo usage: stdout-command ^| %0 command
echo by hishidama 2007-10-26
exit/b 1
)

set LIST=
for /f "delims=" %%i in ('findstr .*') do call :add %%i
%* %LIST%
exit/b

:add
if "%LIST%"=="" (
set LIST=%*
) else (
set LIST=%LIST% %*
)