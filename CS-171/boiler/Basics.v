Inductive day : Type :=
  | monday
  | tuesday
  | wednesday
  | thursday
  | friday
  | saturday
  | sunday.

Definition next_working_day (d : day) : day :=
match d with
  | monday => tuesday
  | tuesday => wednesday
  | wednesday => thursday
  | thursday => friday
  | friday => saturday
  | saturday => sunday
  | sunday => monday
end.

Compute (next_working_day monday).

Compute (next_working_day thursday).

Example test_next_working_day : (next_working_day (next_working_day monday)) = wednesday.
Proof.
  simpl. reflexivity.
Qed.



