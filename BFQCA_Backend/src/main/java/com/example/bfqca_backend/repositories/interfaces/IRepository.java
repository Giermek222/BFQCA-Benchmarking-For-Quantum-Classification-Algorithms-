package com.example.bfqca_backend.repositories.interfaces;

import com.mysql.cj.xdevapi.PreparableStatement;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Types;

public interface IRepository<T> {

    default void setDouble(final PreparedStatement insertStatement, final int parameterIndex, final Double value) throws SQLException {
        if (value == null || value.isNaN()) {
            insertStatement.setNull(parameterIndex, Types.NUMERIC);
            return;
        }
        insertStatement.setDouble(parameterIndex, value);
    }

    default void setString(final PreparedStatement insertStatement, final int parameterIndex, final String value) throws SQLException {
        if (value == null) {
            insertStatement.setNull(parameterIndex, Types.VARCHAR);
            return;
        }
        insertStatement.setString(parameterIndex, value);
    }

    default void setInteger(final PreparedStatement insertStatement, final int parameterIndex, final Integer value) throws SQLException {
        if (value == null) {
            insertStatement.setNull(parameterIndex, Types.NUMERIC);
            return;
        }
        insertStatement.setInt(parameterIndex, value);
    }

    default void setLong(final PreparedStatement insertStatement, final int parameterIndex, final Long value) throws SQLException {
        if (value == null) {
            insertStatement.setNull(parameterIndex, Types.NUMERIC);
            return;
        }
        insertStatement.setLong(parameterIndex, value);
    }

}
