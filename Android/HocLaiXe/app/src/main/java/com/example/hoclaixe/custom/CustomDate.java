package com.example.hoclaixe.custom;

import android.app.DatePickerDialog;
import android.app.Dialog;
import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.support.v4.app.FragmentActivity;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.LinearLayout;

import com.example.hoclaixe.R;
import com.example.hoclaixe.util.Utils;

import java.util.Calendar;


public class CustomDate extends LinearLayout {
    Button btnChonNgay = null;
    EditText edtNgay = null;

    public CustomDate(final Context context, AttributeSet attrs) {
        super(context,attrs);
        LayoutInflater inflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        if(inflater != null){
            inflater.inflate(R.layout.custom_date, this);
            edtNgay = findViewById(R.id.edNgay);
            btnChonNgay = findViewById(R.id.btnChonNgay);
            btnChonNgay.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    DialogFragment newFragment = new DatePickerFragment();
                    newFragment.show(((FragmentActivity) context).getSupportFragmentManager(), "timePicker");
                }
            });
        }
    }

    public String getDate() {
        return edtNgay.getText().toString();
    }

    public static class DatePickerFragment extends DialogFragment
            implements DatePickerDialog.OnDateSetListener {
        final Calendar myCalendar = Calendar.getInstance();

        @Override
        public Dialog onCreateDialog(Bundle savedInstanceState) {
            int year = myCalendar.get(Calendar.YEAR);
            int month = myCalendar.get(Calendar.MONTH);
            int day = myCalendar.get(Calendar.DAY_OF_MONTH);

            return new DatePickerDialog(getActivity(), this, year, month, day);
        }

        public void onDateSet(DatePicker view, int year, int month, int day) {
            myCalendar.set(Calendar.YEAR, year);
            myCalendar.set(Calendar.MONTH, month);
            myCalendar.set(Calendar.DAY_OF_MONTH, day);
            updateLabel();
        }

        private void updateLabel() {
            EditText edNgay = (EditText) getActivity().findViewById(R.id.edNgay);
            edNgay.setText(Utils.dinhDangNgay.format(myCalendar.getTime()));
        }
    }
}
