package com.example.bfqca_backend.models.filters;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;

@Getter
@Setter
@JsonInclude(JsonInclude.Include.NON_NULL)
public class RestFilter implements Serializable {

    @JsonProperty(value = "problem")
    private String problem;

    @JsonProperty(value = "algorithmName")
    private String algorithmname;


}
