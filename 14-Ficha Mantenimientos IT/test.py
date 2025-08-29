

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm, 5cm,3cm,5cm,1cm" style="table_sub1_two">
                        <tr>
                            <td><para style="text1"><b>No. DPI:</b> </para></td>
                            <td><para style="text2"> {{answers.6615585e61a9b62cef0df586}}</para></td>
                            <td><para style="text1"><b>Extendida En:</b> </para></td>
                            <td><para style="text2"> {{answers.6615585e61a9b62cef0df587}}</para></td>
                            <td></td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,5cm,11cm,1cm" style="parrafo">  
            <tr>
                <td></td>    
                <td><para style="text1"><b>Dirección De Domicilio:</b> </para></td>
                <td><para style="text2"> {{answers.6616e00f3c8a9e5a9a0df659}}</para></td>
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="6cm,2.2cm,3.8cm,4cm" style="table_sub1_two">
                        <tr>
                            <td><para style="text1"><b>Por Emergencias Llamar al Tel.</b> </para></td>
                            <td><para style="text2"> {{answers.66155a40831113f20ad09c42}}</para></td>
                            <td><para style="text1"><b>Nombre Completo:</b></para></td>
                            <td><para style="text4"> {{answers.6615800b667b208e8fdc3b53}}</para></td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm,13cm" style="table_sub2_two">
                        <tr>
                            <td><para style="text1"><b>Parentesco:</b> </para></td>
                            <td><para style="text2"> {{answers.661db9b6b0dd78f88d815b1f}}</para></td>                                                                                    
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

          {% set casado = "" %}
          {% set soltero = "" %}
          {% set unido = "" %}
          {% set viudo = "" %}
          {% set divorciado = "" %}

          {% if answers.66155b5425e17960e16f7c09 == "Casado" %}
            {% set casado = "✓" %}
          {% elif answers.66155b5425e17960e16f7c09 == "Soltero" %}
            {% set soltero = "✓" %}
          {% elif answers.66155b5425e17960e16f7c09 == "Unido" %}
            {% set unido = "✓" %}
          {% elif answers.66155b5425e17960e16f7c09 == "Viudo" %}
            {% set viudo = "✓" %}
          {% elif answers.66155b5425e17960e16f7c09 == "Divorciado" %}
            {% set divorciado = "✓" %}
          {% endif %}

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm,2cm,0.5cm,2cm,0.5cm,2cm,0.5cm,2cm,0.5cm,2.5cm,0.5cm" style="table_sub3_two">
                        <tr>
                            <td><para style="text1"><b>Estado Civil:</b> </para></td>
                            <td><para style="text3"><b>Casado:  </b></para></td>
                            <td>{{casado}}</td>
                            <td><para style="text3"><b>Soltero: </b></para></td>
                            <td>{{soltero}}</td>
                            <td><para style="text3"><b>Unido: </b></para></td>
                            <td>{{unido}}</td>
                            <td><para style="text3"><b>Viudo: </b></para></td>
                            <td>{{viudo}}</td>
                            <td><para style="text3"><b>Divorciado: </b></para></td>
                            <td>{{divorciado}}</td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm,2.5cm,4.5cm,3cm,3cm" style="table_sub2_two">
                       <tr>
                            <td><para style="text1"><b>Nombre de Conyugue:</b> </para></td>
                            <td><para style="text2"> {{answers.66157cec7372e2938d5399b1}}</para></td>
                            <td></td>
                            <td><para style="text1"><b>Cuanto Hijos Tiene:</b> </para></td>
                            <td><para style="text2"> {{answers.6615800b667b208e8fdc3b4a}}</para></td>
                            <td></td>
                        </tr>

                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm,2.5cm,2cm,2.5cm,3cm,3cm" style="table_sub4_two">
                        <tr>
                            <td><para style="text1"><b>NIT:  </b></para></td>
                            <td><para style="text2"> {{answers.6615585e61a9b62cef0df589}}</para></td>
                            <td><para style="text1"><b>Tipo de Sangre: </b></para></td>
                            <td><para style="text2"> {{answers.6616dd74bcb3a8de81d09c51}}</para></td>
                            <td><para style="text1"><b>No. Afiliación IGSS: </b></para></td>
                            <td><para style="text2"> {{answers.66155a40831113f20ad09c3f}}</para></td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm, 2.5cm,5.5cm,5cm,1cm" style="table_sub1_two">
                        <tr>
                            <td><para style="text1"><b>Carnet IRTRA:</b> </para></td>
                            <td><para style="text2"> {{answers.66155a40831113f20ad09c40}}</para></td>
                            <td><para style="text1"><b>Fecha de Vencimiento:</b> </para></td>
                            <td><para style="text2"> {{answers.66155a40831113f20ad09c41}}</para></td>
                            <td></td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="3cm, 2.5cm,5.5cm,5cm,1cm" style="table_sub1_two">
                        <tr>
                            <td><para style="text1"><b>No. Licencia:</b> </para></td>
                            <td><para style="text2"> {{answers.661559188f18735bd1d09c4d}}</para></td>
                            <td><para style="text1"><b>Vigencia de Licencia:</b> </para></td>
                            <td><para style="text2"> {{answers.661559188f18735bd1d09c4e}}</para></td>
                            <td></td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,3cm,13cm,1cm" style="parrafo">  
            <tr> 
                <td></td>
                <td><para style="text1"><b>Puesto Actual:</b> </para></td>
                <td><para style="text2"> {{answers.6615800b667b208e8fdc3b4d}}</para></td>
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,6cm,10cm,1cm" style="parrafo">  
            <tr>
                <td></td> 
                <td><para style="text1"><b>Ultimos Estudios Realizados:</b> </para></td>
                <td><para style="text2"> {{answers.6615800b667b208e8fdc3b4e}}</para></td> 
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,6cm,10cm,1cm" style="parrafo">  
            <tr>
                <td></td>  
                <td><para style="text1"><b>Institucion/Universidad de Estudios:</b> </para></td>
                <td><para style="text2"> {{answers.6615800b667b208e8fdc3b4f}}</para></td> 
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,6cm,10cm,1cm" style="parrafo">  
            <tr>
                <td></td>  
                <td><para style="text1"><b> Maestría/Certificados/Cursos:</b> </para></td>
                <td><para style="text2"> {{answers.6615800b667b208e8fdc3b50}}</para></td> 
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,6cm,10cm,1cm" style="parrafo">  
            <tr>
                <td></td>  
                <td><para style="text1"><b>Accidentes, Incapacidad, viaje, trabajo, entregar cheque a :</b> </para></td>
                <td><para style="text2"> {{answers.66158101a1649c0096d09c05}}</para></td>
                <td></td>   
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="5cm,1cm,2cm,3cm,2cm,3cm,1cm" style="table_sub6_two">
                        <tr>
                            <td><para style="text1"><b>Autoriza Recoger Cheque:</b> </para></td>
                            <td>{{answers.661e8a9702a90058c0f11a58}}</td>
                            <td><para style="text3"><b>DPI: </b></para></td>
                            <td>{{answers.661e8a9702a90058c0f11a59}}</td>
                            <td><para style="text3"><b>Teléfono: </b></para></td>
                            <td>{{answers.661db9b6b0dd78f88d815b21}}</td>
                            <td></td> 
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,8cm,8cm,1cm" style="parrafo">  
            <tr>
                <td></td>   
                <td><para style="text1"><b> Fecha de Inicio Laboral en SELECOM:</b> </para></td>
                <td><para style="text2"> {{answers.661db9b6b0dd78f88d815b22}}</para></td> 
                <td></td>
            </tr> 
        </blockTable>

        <spacer length="0.2cm"/>
        <blockTable colWidths="0.4cm,8cm,8cm,1cm" style="parrafo">  
            <tr>
                <td></td>   
                <td><para style="text1"><b> Fecha de Baja Laboral en SELECOM:</b> </para></td>
                <td><para style="text2"> {{answers.661db9b6b0dd78f88d815b23}}</para></td> 
                <td></td>
            </tr> 
        </blockTable>

          {% set renuncia = "" %}
          {% set despido = "" %}
          {% set abandono = "" %}
          {% set enfermedad = "" %}

          {% if answers.661e8861217505025fb73bda == "Renuncia" %}
            {% set renuncia = "✓" %}
          {% elif answers.661e8861217505025fb73bda == "Despido" %}
            {% set despido = "✓" %}
          {% elif answers.661e8861217505025fb73bda == "Abandono de Trabajo" %}
            {% set abandono = "✓" %}
          {% elif answers.661e8861217505025fb73bda == "Enfermedades /otros motivos" %}
            {% set enfermedad = "✓" %}
          {% endif %}

        <spacer length="0.2cm"/>
        <blockTable colWidths="17cm">  
            <tr>
                <td>
                    <blockTable colWidths="2.5cm,2.2cm,1cm,2.2cm,1cm,2.5cm,1cm,2.6cm,1cm" style="table_sub7_two">
                        <tr>
                            <td><para style="text1"><b>Motivo Baja:</b> </para></td>
                            <td><para style="text3"><b>Renuncia:  </b></para></td>
                            <td>{{renuncia}}</td>
                            <td><para style="text3"><b>Despido: </b></para></td>
                            <td>{{despido}}</td>
                            <td><para style="text3"><b>Abandono: </b></para></td>
                            <td>{{abandono}}</td>
                            <td><para style="text3"><b>IDF: </b></para></td>
                            <td>{{enfermedad}}</td>
                        </tr>
                    </blockTable>
                </td>
            </tr> 
        </blockTable>
        
        
        
        
    <blockTable colWidths="15cm" style="table_Header">        
        <tr>
            <td>
                <blockTable colWidths="4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm" style="table_sub3_two">
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </blockTable>
                <spacer length="0.1cm"/>  
                <blockTable colWidths="4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm" style="table_sub3_two">
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </blockTable>
                <spacer length="0.1cm"/>  
                <blockTable colWidths="4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm,4cm,0.5cm,0.5cm" style="table_sub3_two">
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </blockTable>
            </td>
        </tr> 
    </blockTable>