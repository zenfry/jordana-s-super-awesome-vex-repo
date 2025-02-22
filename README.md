# jordana-s-super-awesome-vex-repo
Autonomous Period
* Runs automatically when the match starts (before driver control).
* Displays "Autonomous Running" on the Brain screen.
* Moves forward for 2 seconds, then stops.

Driver-Controlled Period
* Displays "Driver Control Running" on the Brain screen.
* Arcade drive system:
    * axis3 (joystick up/down) controls forward/backward movement.
    * axis1 (joystick left/right) controls turning.
    * Motors calculate speed based on joystick values.
* Conveyor Belt Controls:
    * L1 moves conveyor forward.
    * R1 moves conveyor backward.
    * If no button is pressed, the conveyor holds position.
